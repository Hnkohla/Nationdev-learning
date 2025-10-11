"""
Core models for NationDev Learning Platform
Author: Hlumile Khanyo Nkohla (hnkohla)
"""
from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    """Represents an educational course in the platform."""
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title