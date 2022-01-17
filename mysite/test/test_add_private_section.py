from django.test import TestCase
from mysite.models.segment import DefinedSegment, Segment
from mysite.models.range import Range
from mysite.models.point import Point
import os
from mysite.views.add_private_section_view import AddPrivateSection
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'


class TestAddPrivateSection(TestCase):
    def setUp(self):
        bartek = User.objects.create_user(email='bartek@gmail.com', password='Oo', name='Bartek', surname='Nowak')
        bartek.save()
        Tourist(birth_date='2000-10-10', user=bartek).save()

    def x(self):
        pass