from django.test import TestCase
from django.contrib.auth import login, authenticate
from django.urls import reverse

from slmApp.models import CustomUser
from slmApp.forms import LoginForm

class LoginTest(TestCase):
    @classmethod
    def setUp(cls):
        user = CustomUser.objects.create_user('testUser', 'admin@testmail.com', 'testUser')
        user.first_name = 'first'
        user.last_name = 'last'
        user.save()
        admin = CustomUser.objects.create_superuser('testAdmin', 'admin@testmail.com', 'testAdmin')
        admin.first_name = 'first'
        admin.last_name = 'last'
        admin.save()

    def test_user_login(self):
        login = self.client.login(username='testUser', password='testUser')
        response = self.client.get(reverse('student'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(str(response.context['user']), 'testUser')
    
    def test_admin_login(self):
        login = self.client.login(username='testAdmin', password='testAdmin')
        response = self.client.get(reverse('instructor'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(str(response.context['user']), 'testAdmin')