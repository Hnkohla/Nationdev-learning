from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Course, BlogPost, CourseReview
from .forms import CustomUserCreationForm, CourseReviewForm

def nationdev(request):
    # Redirect to courses page for the Explore Courses button
    return redirect('courses')

def about(request):
    try:
        return render(request, 'core/about.html')
    except Exception as e:
        messages.error(request, 'An error occurred while loading the about page.')
        return render(request, 'core/about.html', {'error': True})

def home(request):
    if request.path == '/home/':
        return redirect('home')  # Redirect /home/ to root URL
        
    try:
        featured_courses = Course.objects.filter(featured=True, active=True).select_related()[:3]
        latest_posts = BlogPost.objects.filter(
            published_date__isnull=False
        ).select_related('author').order_by('-published_date')[:2]
        
        context = {
            'featured_courses': featured_courses,
            'latest_posts': latest_posts,
            'page_title': 'Welcome to NationDev',
        }
        return render(request, 'core/home.html', context)
    except Exception as e:
        messages.error(request, 'An error occurred while loading the homepage.')
        return render(request, 'core/home.html', {'error': True})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def course_detail(request, pk):
    try:
        course = get_object_or_404(Course.objects.select_related(), pk=pk, active=True)
        user_review = None
        review_form = None
        can_enroll = True
        
        if request.user.is_authenticated:
            user_review = course.reviews.filter(user=request.user).select_related('user').first()
            if not user_review:
                enrolled_count = course.reviews.count()
                can_enroll = enrolled_count < course.enrollment_capacity
                
            review_form = CourseReviewForm(instance=user_review) if user_review else CourseReviewForm()
            
            if request.method == 'POST':
                if not can_enroll and not user_review:
                    messages.error(request, 'Sorry, this course has reached its enrollment capacity.')
                    return redirect('course-detail', pk=pk)
                    
                review_form = CourseReviewForm(request.POST, instance=user_review)
                if review_form.is_valid():
                    review = review_form.save(commit=False)
                    review.course = course
                    review.user = request.user
                    review.save()
                    messages.success(request, 'Your review has been saved.')
                    return redirect('course-detail', pk=pk)
                else:
                    messages.error(request, 'Please correct the errors below.')
        
        context = {
            'course': course,
            'review_form': review_form,
            'user_review': user_review,
            'is_enrolled': request.user.is_authenticated and user_review is not None,
            'can_enroll': can_enroll,
            'page_title': f'Course: {course.title}',
        }
        return render(request, 'core/course_detail.html', context)
        
    except Exception as e:
        messages.error(request, 'An error occurred while loading the course details.')
        return redirect('courses')

@login_required
def course_content(request, pk):
    course = get_object_or_404(Course, pk=pk)
    user_review = course.reviews.filter(user=request.user).first()
    
    if not user_review:
        messages.error(request, 'You must be enrolled in this course to access its content.')
        return redirect('course-detail', pk=pk)
    
    return render(request, 'core/course_content.html', {
        'course': course
    })

class CourseListView(ListView):
    model = Course
    template_name = 'core/course_list.html'
    context_object_name = 'courses'
    paginate_by = 9
    
    def get_queryset(self):
        queryset = Course.objects.filter(active=True).select_related()
        level = self.request.GET.get('level')
        if level in dict(Course.LEVEL_CHOICES):
            queryset = queryset.filter(level=level)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Our Courses'
        context['levels'] = Course.LEVEL_CHOICES
        context['selected_level'] = self.request.GET.get('level')
        return context

class BlogListView(ListView):
    model = BlogPost
    template_name = 'core/blog_list.html'
    context_object_name = 'posts'
    paginate_by = 6
    
    def get_queryset(self):
        return BlogPost.objects.filter(
            published_date__isnull=False
        ).select_related('author').order_by('-published_date')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Blog Posts'
        return context

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'core/blog_detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'slug'

@login_required
def profile(request):
    user_reviews = CourseReview.objects.filter(user=request.user).select_related('course')
    enrolled_courses = Course.objects.filter(id__in=user_reviews.values_list('course', flat=True))
    
    return render(request, 'core/profile.html', {
        'user_reviews': user_reviews,
        'enrolled_courses': enrolled_courses
    })
