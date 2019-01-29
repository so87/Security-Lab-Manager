from django.test import TestCase
from django.db import models
from slmApp.models import Users, Classes, Exercises

class M2MThroughTest(TestCase):
    def setUp(self):
        self.simon = Users.objects.create(name='Joe Owens', email="so87@evansville.edu", password="joe", privilege="user")