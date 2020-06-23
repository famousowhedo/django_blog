from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date= models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=30 ,choices=(
        ('male', 'Male'),
        ('female','Female'),

    ))


    def __str__(self):
        return self.title
    