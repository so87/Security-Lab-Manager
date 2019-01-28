from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoginView, name='login'),
    path('student/', views.StudentView, name='student'),
    path('instructor/', views.InstructorView, name='instructor'),
    path('instructor/settings/', views.InstructorSettingsView, name='settings'),
]