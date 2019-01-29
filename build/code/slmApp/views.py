import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic

from slmApp.models import Users,Classes,Exercises,Settings
from slmApp.forms import LoginForm
from django.views import generic

def LoginView(request):
    users = Users.objects.all()

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required and make sure it matches a username/password
            users.email = form.cleaned_data['email']
            users.password = form.cleaned_data['password']

            # logged in
            if (user.email in users.email) & (user.password in users.password):
                return HttpResponseRedirect('/login/student/')
            # not valid
            else:
                return HttpResponseRedirect('/login/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    return render(request, 'login.html', {'users': users, 'form': form})

def StudentView(request):
    classes = Classes.objects.all()
    return render(request, 'student.html', {'classes': classes})

def InstructorView(request):
    classes = Classes.objects.all()
    return render(request, 'admin.html', {'classes': classes})

def InstructorSettingsView(request):
    settings = Settings.objects.all()
    return render(request, 'admin_settings.html', {'settings': settings})

def makeData():
    u1 = Users()
    u1.name = 'Simon Owens'
    u1.email = 'simonowens157@gmail.com'
    u1.password = 'simon'
    u1.privilege = 'user'
    u1.save()
    u2 = Users()
    u2.name = 'Mark Randall'
    u2.email = 'mark@evansville.edu'
    u2.password = 'simon'
    u2.privilege = 'admin'
    u2.save()
    u3 = Users()
    u3.name = 'Packman'
    u3.email = 'packman@evansville.edu'
    u3.password = 'simon'
    u3.privilege = 'user'
    u3.save()
    u4 = Users()
    u4.name = 'Ron Doberts'
    u4.email = 'rondoberts@evansville.edu'
    u4.password = 'simon'
    u4.privilege = 'user'
    u4.save()
    u5 = Users()
    u5.name = 'Dr. Hwang'
    u5.email = 'hwang@evansville.edu'
    u5.password = 'simon'
    u5.privilege = 'admin'
    u5.save()

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
    c1.save()
    c1.name = 'Web Security Fall 2018'
    c1.description = 'Taught by Dr. Hwang'
    c1.instructor.add(u5)
    c1.exercises.add(e1)
    c1.exercises.add(e2)
    c1.students.add(u1)
    c1.students.add(u2)
    c1.save()
    c2 = Classes()
    c2.save()

    c2.name = 'Desktop Security Fall 2018'
    c2.description = 'Taught by Mr. Randall'
    c2.instructor.add(u2)
    c2.exercises.add(e3)
    c2.students.add(u1)
    c2.students.add(u2)
    c2.students.add(u3)
    c2.students.add(u4)
    c2.save()
    c3 = Classes()
    c3.save()

    c3.name = 'Web Security Spring 2019'
    c3.description = 'Taught by Dr. Hwang'
    c3.instructor.add(u5)
    c3.exercises.add(e1)
    c3.exercises.add(e2)
    c3.exercises.add(e4)
    c3.students.add(u1)
    c3.students.add(u4)
    c3.save()

    s = Settings()
    s.name = "Settings"
    s.ram = "4000"
    s.cores = "4"
    s.instances = "4"
    s.save()
