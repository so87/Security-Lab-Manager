import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from slmApp.models import Classes, Exercises, Submissions, Settings, CustomUser
from slmApp.forms import LoginForm,SignUpForm,SubmitAnswer

from slmApp.exercises import command

# The main login page
def LoginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
    form = LoginForm()
    return render(request, 'login.html', {'form': form})
# Decides if should go to instructor or student page
def RedirectLogin(request):
    if request.user.is_superuser == True:
        return HttpResponseRedirect(reverse('instructor'))
    else:
        return HttpResponseRedirect(reverse('student'))

# Signup forms for users and admins
def SignupView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('student')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
def SignupAdminView(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            user.is_superuser = True
            user.save()
            login(request, user)
            return redirect('instructor')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

# Correct Classes show up based on who you are
@login_required
def StudentView(request):
    classes = Classes.objects.filter(students=request.user)
    form = SubmitAnswer()
    return render(request, 'student.html', {'classes': classes, 'form': form})
@login_required
def InstructorView(request):
    classes = Classes.objects.filter(instructor=request.user)
    return render(request, 'admin.html', {'classes': classes})
@login_required
def InstructorSettingsView(request):
    settings = Settings.objects.all()
    return render(request, 'admin_settings.html', {'settings': settings})

# submitting answers to the exercises
@login_required
def SubmitExerciseView(request, Cpk, Epk):
    if request.method == 'POST':
        form = SubmitAnswer(request.POST)
        if form.is_valid():
            user_submission = form.cleaned_data.get("submitted")
            exercise = Exercises.objects.get(pk=Epk)
            class_inst = Classes.objects.get(pk=Cpk)
            submission, created = Submissions.objects.get_or_create(student=request.user,exercises=exercise,classes=class_inst)
            submission.submitted = user_submission
            submission.save()
    else:
        form = SubmitAnswer()
    return redirect('student')

@login_required
def SubmissionsView(request, Cpk, Epk):
    if request.method == 'POST':
        submissions = Submissions.objects.filter(classes=Cpk).filter(exercises=Epk)
        return render(request, 'details_submissions.html', {'submissions': submissions})

@login_required
def GradebookView(request, Cpk):
    classes = Classes.objects.get(pk=Cpk)
    students = classes.students.all()
    exercises = classes.exercises.all()
    
    # exercise is the row
    for exercise in exercises:
        # students are the columns
        for student in students:
            # check if student submitted an answer for this exercise
            grades += Submissions.objects.filter(classes=Cpk).filter(exercises=exercise.id)

            # decide if user got the correct answer or not (zero if not submitted)
    
    print(grades)
    print(students)
    print(exercises)
    return render(request, 'details_gradebook.html', {'classes': classes,})

# Viewing Database Items
@login_required
def StudentsView(request):
    students = CustomUser.objects.all()
    return render(request, 'details_students.html', {'students': students})
@login_required
def ExercisesView(request):
    exercises = Exercises.objects.all()
    return render(request, 'details_exercises.html', {'exercises': exercises})
@login_required
def ClassesView(request):
    classes = Classes.objects.all()
    return render(request, 'details_classes.html', {'classes': classes})

# Editing Database Items

class ClassesCreate(CreateView):
    model = Classes
    fields = '__all__'

class ClassesUpdate(UpdateView):
    model = Classes
    fields = '__all__'

class ClassesDelete(DeleteView):
    model = Classes
    fields = '__all__'
    success_url = reverse_lazy('instructor')

class ExercisesCreate(CreateView):
    model = Exercises
    fields = '__all__'

class ExercisesUpdate(UpdateView):
    model = Exercises
    fields = '__all__'

class ExercisesDelete(DeleteView):
    model = Exercises
    fields = '__all__'
    success_url = reverse_lazy('instructor')

class CustomUserCreate(CreateView):
    model = CustomUser
    fields = '__all__'

class CustomUserUpdate(UpdateView):
    model = CustomUser
    fields = '__all__'

class CustomUserDelete(DeleteView):
    model = CustomUser
    fields = '__all__'
    success_url = reverse_lazy('instructor')
@login_required
def StartExercise(request, StudentPK, ExercisePK):
    # ensure the user has authorization to start that exercise
    student = CustomUser.objects.get(pk=StudentPK)
    # finds student and their exercise to run
    exercise = Exercises.objects.get(pk=ExercisePK)
    exercise_name = exercise.name
    exercise_name = exercise_name.lower()
    exercise_name = exercise_name.replace(" ", "")
    student_name = student.username

    # ensure the student isn't already running another container
    if (student.exercises_running == 1):
        return redirect('student')

    # run the exercise
    status = command.run_container(student_name, exercise_name)

    # update containers running if it staretd successfully
    if(status != 1):
        student.exercises_running = 1
        student.save()
    print("Exercises open: "+str(student.exercises_running))
    # give the user back their port so they know where to go
    return redirect('student')
@login_required
def StopExercise(request, StudentPK, ExercisePK):
    # ensure the user has authorization to start that exercise
    student = CustomUser.objects.get(pk=StudentPK)
    # finds student and their exercise to run
    exercise = Exercises.objects.get(pk=ExercisePK)
    exercise_name = exercise.name
    exercise_name = exercise_name.lower()
    exercise_name = exercise_name.replace(" ", "")
    student_name = student.username

    # run the exercise
    status = command.stop_container(student_name, exercise_name)

    # update containers running if it staretd successfully
    if(status == 0):
        student.exercises_running = 0
        student.save()
    print("Exercises open: "+str(student.exercises_running))
    return redirect('student')
@login_required
def RestartExercise(request, StudentPK, ExercisePK):
    # ensure the user has authorization to start that exercise
    student = CustomUser.objects.get(pk=StudentPK)
    # finds student and their exercise to run
    exercise = Exercises.objects.get(pk=ExercisePK)
    exercise_name = exercise.name
    exercise_name = exercise_name.lower()
    exercise_name = exercise_name.replace(" ", "")
    student_name = student.username

    # restart the exercise
    status = command.restart_container(student_name, exercise_name)

    # update containers running if it staretd successfully
    if(status == 0):
        student.exercises_running = 0
        student.save()
    print("Exercises open: "+str(student.exercises_running))
    return redirect('student')

# Sample data to interact with
def create_data():
    u4 = CustomUser.objects.create_user('johndoe', 'myemail@crazymail.com', 'johndoe')
    u4.first_name = 'John'
    u4.last_name = 'Doe'
    u4.save()
    u5 = CustomUser.objects.create_user('dumby', 'myemail@crazymail.com', 'dumby')
    u5.first_name = 'Dumby'
    u5.last_name = 'Dumbdumb'
    u5.save()
    u6 = CustomUser.objects.create_user('packman', 'so87@evansville.edu', 'packman')
    u6.first_name = 'Packman'
    u6.last_name = 'Jones'
    u6.save()
    u1 = CustomUser.objects.create_superuser('mark', 'myemail@crazymail.com', 'mark')
    u1.first_name = 'mark'
    u1.last_name = 'randall'
    u1.save()
    u2 = CustomUser.objects.create_superuser('deborah', 'myemail@crazymail.com', 'deborah')
    u2.first_name = 'deborah'
    u2.last_name = 'hwang'
    u2.save()
    u3 = CustomUser.objects.create_superuser('ron', 'myemail@crazymail.com', 'doberts')
    u3.first_name = 'ron'
    u3.last_name = 'doberts'
    u3.save()

    e1 = Exercises()
    e1.name = 'SQL Injection'
    e1.description = 'Give an example of SQL injection on port 8882'
    e1.answer = 'asdfasdf1231234'
    e1.save()
    e2 = Exercises()
    e2.name = 'SQL Injection 2'
    e2.description = 'Give an example of SQL injection on port 12834'
    e2.answer = 'asdfasdf1231234'
    e2.save()
    e3 = Exercises()
    e3.name = 'XSS 1'
    e3.description = 'Give an example of SQL injection on port 8582'
    e3.answer = 'asdfasdf1231234'
    e3.save()
    e4 = Exercises()
    e4.name = 'Buffer Overflow'
    e4.description = 'Give an example of Buffer overflow on port 8812'
    e4.answer = 'asdfasdf1231234'
    e4.save()

    c1 = Classes()
    c1.name = 'Desktop Security Fall 2017'
    c1.description = 'Taught by Ron Doberts'
    c1.save()
    c1.instructor.add(u2)
    c1.exercises.add(e1)
    c1.exercises.add(e2)
    c1.students.add(u4)
    c1.students.add(u5)
    c1.save()
    c2 = Classes()
    c2.name = 'Desktop Security Fall 2018'
    c2.description = 'Taught by Mr. Randall'
    c2.save()
    c2.instructor.add(u1)
    c2.exercises.add(e3)
    c2.students.add(u4)
    c2.students.add(u5)
    c2.students.add(u6)
    c2.save()
    c3 = Classes()
    c3.name = 'Web Security Spring 2019'
    c3.description = 'Taught by Dr. Hwang'
    c3.save()
    c3.instructor.add(u2)
    c3.exercises.add(e1)
    c3.exercises.add(e2)
    c3.exercises.add(e4)
    c3.students.add(u4)
    c3.students.add(u6)
    c3.save()

    s = Settings()
    s.name = "Settings"
    s.ram = "4000"
    s.cores = "4"
    s.instances = "4"
    s.save()
    

def DataView(request):
    create_data()
    return render(request, 'create_data.html')