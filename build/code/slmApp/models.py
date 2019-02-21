from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    # add additional fields in here
    def __str__(self):
        return self.username

class Settings(models.Model):
    name = models.CharField(max_length=30)
    ram = models.IntegerField()
    cores = models.IntegerField()
    instances = models.IntegerField()

    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        # allows table to be shown in admin site
        return reverse('settings-detail', args=[str(self.id)])

class Exercises(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        # allows table to be shown in admin site
        return reverse('exercise-detail', args=[str(self.id)])

class Classes(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    students = models.ManyToManyField('CustomUser', blank=True, related_name='user')
    instructor = models.ManyToManyField('CustomUser', blank=True, related_name='instructor')
    exercises = models.ManyToManyField('Exercises', blank=True, related_name='exercises')
    
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        # allows table to be shown in admin site
        return reverse('class-detail', args=[str(self.id)])
