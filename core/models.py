from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Course(models.Model):
    LEVEL_CHOICES = [
        ('BEG', 'Beginner'),
        ('INT', 'Intermediate'),
        ('ADV', 'Advanced'),
        ('EXP', 'Expert'),
    ]

    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    short_description = models.CharField(max_length=200, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration_weeks = models.IntegerField(help_text="Course duration in weeks")
    level = models.CharField(max_length=3, choices=LEVEL_CHOICES)
    image = models.ImageField(upload_to='course_images/%Y/%m/', null=True, blank=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    enrollment_capacity = models.PositiveIntegerField(default=100)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']



class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    summary = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='blog_images/%Y/%m/', null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    last_modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    tags = models.CharField(max_length=200, blank=True, help_text="Comma-separated tags")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

class CourseReview(models.Model):
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=RATING_CHOICES)
    review_text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_date']
        unique_together = ['user', 'course']

    def __str__(self):
        return f"Review by {self.user.username} for {self.course.title}"