from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class courses(models.Model):
    
    courses = models.CharField(max_length=100)
    detail =models.TextField()
    
    

    def get_absolute_url(self):
            return reverse('course-detail', kwargs={'pk': self.pk})
