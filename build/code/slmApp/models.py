from django.db import models

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

class Users(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, unique=True, db_index=True, primary_key=True)
    privilege_levels = [("user", "user"), ("admin","admin")]
    privilege = models.CharField(max_length=10, choices=privilege_levels)
    
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.email
    def get_absolute_url(self):
        # allows table to be shown in admin site
        return reverse('user-detail', args=[str(self.id)])

class Classes(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    instructor = models.ManyToManyField(Users, related_name='instructors')
    exercises = models.ManyToManyField(Exercises, related_name='exercises')
    students = models.ManyToManyField(Users,related_name='students')
    
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        # allows table to be shown in admin site
        return reverse('class-detail', args=[str(self.id)])
