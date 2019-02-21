from django.urls import path
from django.conf.urls import url
from . import views
from django.urls import include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', include('django.contrib.auth.urls')), #'function' object is not a mapping
    path('data/', views.DataView, name='data'),
    path('signup/', views.SignupView, name='signup'),
    path('student/', views.StudentView, name='student'),
    path('instructor/', views.InstructorView, name='instructor'),
    path('instructor/settings/', views.InstructorSettingsView, name='settings'),
]