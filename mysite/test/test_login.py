from django.test import TestCase
from mysite.models.user import User
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'


class TestLogin(TestCase):

    def test_not_logged(self):
        response = self.client.get('/profile/', follow=True)
        self.assertRedirects(response, '/login/')
        print(response.status_code)

    def test_uncorrect_logged(self):
        self.client.login(username='bartek@gmail.com', password='Ooo')
        response = self.client.get('/profile/', follow=True)
        self.assertRedirects(response, '/login/')
        print(response.status_code)

    def test_correct_logged(self):
        self.client.force_login(User.objects.get_or_create(email='testuser')[0])
        self.client.get('/profile/', follow=True)
        self.assertTemplateUsed('profile.html')