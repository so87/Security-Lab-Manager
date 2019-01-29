from django.contrib import admin
from slmApp.models import Users,Classes,Exercises,Settings

# Register your models here.
@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    pass
@admin.register(Exercises)
class ExercisesAdmin(admin.ModelAdmin):
    pass
@admin.register(Classes)
class ClassesAdmin(admin.ModelAdmin):
    pass
@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    pass