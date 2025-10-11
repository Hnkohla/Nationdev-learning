"""
Core views for NationDev Learning Platform
Author: Hlumile Khanyo Nkohla (hnkohla)
"""
from django.shortcuts import render
from django.views.generic import ListView
from .models import Course

def home(request):
    """Homepage view showing platform overview."""
    return render(request, 'core/home.html')

def about(request):
    """About page with platform information."""
    return render(request, 'core/about.html')

class CourseListView(ListView):
    """Display list of available courses."""
    model = Course
    template_name = 'core/course_list.html'
    context_object_name = 'courses'