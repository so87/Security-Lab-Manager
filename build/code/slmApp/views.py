import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic

def LoginView(request):
    return render(request, 'login.html', {})

def StudentView(request):
    return render(request, 'student.html', {})

def InstructorView(request):
    return render(request, 'admin.html', {})

def InstructorSettingsView(request):
    return render(request, 'admin_settings.html', {})