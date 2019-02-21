from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from slmApp.models import Classes,Exercises,Settings,CustomUser
from slmApp.forms import LoginForm


# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    add_form = LoginForm
    form = LoginForm
    model = CustomUser

class ExercisesAdmin(admin.ModelAdmin):
    model = Exercises

class ClassesAdmin(admin.ModelAdmin):
    model = Classes

class SettingsAdmin(admin.ModelAdmin):
    model = Settings

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Exercises, ExercisesAdmin)
admin.site.register(Classes, ClassesAdmin)
admin.site.register(Settings, SettingsAdmin)