"""
URL patterns for core app
Author: Hlumile Khanyo Nkohla (hnkohla)
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('courses/', views.CourseListView.as_view(), name='course_list'),
]