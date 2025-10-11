from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Make home the default landing page
    path('home/', views.home, name='home-redirect'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('courses/', views.CourseListView.as_view(), name='courses'),
    path('courses/<int:pk>/', views.course_detail, name='course-detail'),
    path('courses/<int:pk>/content/', views.course_content, name='course-content'),
    path('blog/', views.BlogListView.as_view(), name='blog'),
    path('blog/<slug:slug>/', views.BlogDetailView.as_view(), name='blog-detail'),
    path('about/', views.about, name='about')
]