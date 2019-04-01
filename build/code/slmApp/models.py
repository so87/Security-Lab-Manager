from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse_lazy, reverse

class Settings(models.Model):
    name = models.CharField(max_length=30)
    hostname = models.CharField(max_length=30)
    ram = models.IntegerField(validators=[MaxValueValidator(204800), MinValueValidator(512)])
    cores = models.IntegerField(validators=[MaxValueValidator(12), MinValueValidator(1)])
    instances = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(1)])

    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name+" at: "+self.hostname
    def get_absolute_url(self):
        # allows table to be shown in admin site
        return reverse('settings-detail', args=[str(self.id)])

class CustomUser(AbstractUser):
    exercise_running = models.ForeignKey('Exercises',on_delete=models.PROTECT, null=True)
    exercise_port = models.IntegerField(null=True)

    def __str__(self):
        return self.username
    def get_absolute_url(self):
        return reverse('customuser-detail', args=[str(self.id)])

class Submissions(models.Model):
    student = models.ForeignKey('CustomUser',on_delete=models.PROTECT)
    exercises = models.ForeignKey('Exercises',on_delete=models.PROTECT)
    classes = models.ForeignKey('Classes',on_delete=models.PROTECT)
    submitted = models.CharField(max_length=50)
    def filter_students(self, pk_list):
        return self.student.filter(pk__in=pk_list)
    class Meta:
        ordering = ['student']
    def __str__(self):
        return self.exercises.name+": "+self.student.last_name+","+self.student.first_name+": "+self.submitted
    def get_absolute_url(self):
        # allows table to be shown in admin site
        return reverse('submission-detail', args=[str(self.id)])

class Exercises(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    answer = models.CharField(max_length=50)

    def get_submissions(self, pk_list):
        return self.attempted.filter_students(self.attempted, pk_list)

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
    students = models.ManyToManyField('CustomUser', blank=True, related_name='students')
    instructor = models.ManyToManyField('CustomUser', blank=True, related_name='instructor')
    exercises = models.ManyToManyField('Exercises', blank=True, related_name='exercises')
    attempted = models.ManyToManyField('Submissions', blank=True, related_name='attempted')
    
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        # allows table to be shown in admin site
        return reverse('class-detail', args=[str(self.id)])
