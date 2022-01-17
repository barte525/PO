from django.test import TestCase
from mysite.models.user import User, Tourist
from mysite.models.route import Route
from mysite.models
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'


class TestAddPrivateSection(TestCase):
    def setUp(self):
        test = User.objects.create_user(email='test@gmail.com', password='Oo', name='test', surname='test')
        test.save()
        test_tourist = Tourist(birth_date='2000-10-10', user=test)
        test_tourist.save()
        Route(name="test_route", start_date="2020-10-11", end_date="2020-10-11", tourist=test_tourist)

    def test_incorrect_height(self):


