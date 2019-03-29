from django.urls import path
from django.conf.urls import url
from . import views
from django.urls import include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', include('django.contrib.auth.urls')), #'function' object is not a mapping
    path('data/', views.DataView, name='data'),
    
    # Authentication
    path('signup/', views.SignupView, name='signup'),
    path('signup/admin/', views.SignupAdminView, name='signupAdmin'),
    path('profile/', views.RedirectLogin, name='profile'),
    
    # The standard user and admin views
    path('student/', views.StudentView, name='student'),
    path('instructor/', views.InstructorView, name='instructor'),
    
    # Views to create, update, or delete
    path('instructor/classes/', views.ClassesView, name='classes'),
    path('instructor/class/<int:pk>/update/', views.ClassesUpdate.as_view(), name='classes_update'),
    path('instructor/class/<int:pk>/delete/', views.ClassesDelete.as_view(), name='classes_delete'),
    path('instructor/class/create/', views.ClassesCreate.as_view(), name='classes_create'),

    path('instructor/exercises/', views.ExercisesView, name='exercises'),
    path('instructor/exercise/<int:pk>/update/', views.ExercisesUpdate.as_view(), name='exercises_update'),
    path('instructor/exercise/<int:pk>/delete/', views.ExercisesDelete.as_view(), name='exercises_delete'),
    path('instructor/exercise/create/', views.ExercisesCreate.as_view(), name='exercises_create'),
    
    path('instructor/students/', views.StudentsView, name='students'),
    path('instructor/students/<int:pk>/update/', views.CustomUserUpdate.as_view(), name='customUser_update'),
    path('instructor/students/<int:pk>/delete/', views.CustomUserDelete.as_view(), name='customUser_delete'),
    path('instructor/students/create/', views.CustomUserCreate.as_view(), name='customUser_create'),
    
    path('student/submit/<int:Cpk>/<int:Epk>', views.SubmitExerciseView, name='submit'),
    path('instructor/submissions/<int:Cpk>/<int:Epk>', views.SubmissionsView, name='submission_details'),
    path('instructor/gradebook/<int:Cpk>', views.GradebookView, name='gradebook'),

    # Start, Stop, and restart exercises
    path('student/<int:StudentPK>/<int:ExercisePK>/start/', views.StartExercise, name='start_exercise'),
    path('student/<int:StudentPK>/<int:ExercisePK>/restart/', views.RestartExercise, name='restart_exercise'),
    path('student/<int:StudentPK>/<int:ExercisePK>/stop/', views.StopExercise, name='stop_exercise'),

    # Views for settings
    path('instructor/settings/', views.InstructorSettingsView, name='settings'),
]