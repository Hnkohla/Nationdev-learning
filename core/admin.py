from django.contrib import admin
from .models import Course, BlogPost, CourseReview

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'level', 'duration_weeks', 'featured')
    list_filter = ('level', 'featured')
    search_fields = ('title', 'description')
    list_editable = ('featured',)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date', 'published_date')
    list_filter = ('published_date', 'author')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(CourseReview)
class CourseReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'rating', 'created_date')
    list_filter = ('rating', 'created_date')
    search_fields = ('review_text', 'user__username', 'course__title')
