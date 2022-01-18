from django.test import TestCase
from mysite.models.user import User, Tourist
from mysite.models.route import Route
from mysite.views.count_points_view import CountPoints
from mysite.models.segment import Segment, DefinedSegment, CustomSegment
from mysite.models.range import Range
from mysite.models.point import Point
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'


class TestAddPrivateSection(TestCase):
    def setUp(self):
        test = User.objects.create_user(email='test@gmail.com', password='Oo', name='test', surname='test')
        test.save()
        test_tourist = Tourist(birth_date='2000-10-10', user=test)
        test_tourist.save()
        self.route1 = Route(name="test_route1", start_date="2020-10-11", end_date="2020-10-11", tourist=test_tourist)
        self.route1.save()
        self.route2 = Route(name="test_route2", start_date="2020-10-12", end_date="2020-10-12", tourist=test_tourist)
        self.route2.save()
        self.routes = list(Route.objects.filter(tourist=test_tourist))
        murow = Segment(length=1000, range=Range.objects.filter(name="Tatry")[0])
        murow.save()
        self.defined1 = DefinedSegment(segment=murow, points=100, name="test1", start_point=Point.objects.filter(name="Murowaniec")[0],
                                       end_point=Point.objects.filter(name="Czarny staw")[0])
        self.defined1.save()

        murow = Segment(length=1000, range=Range.objects.filter(name="Tatry")[0])
        murow.save()
        self.defined2 = DefinedSegment(segment=murow, points=50, name="test2",
                                       start_point=Point.objects.filter(name="Murowaniec")[0],
                                       end_point=Point.objects.filter(name="Czarny staw")[0])
        self.defined2.save()

        murow = Segment(length=2000, range=Range.objects.filter(name="Tatry")[0])
        murow.save()
        self.custom1 = CustomSegment(segment=murow, start_name="start_name", start_height=100, end_height=500,
                                      end_name="end_name", name="test3", elevation=740)
        self.custom1.save()

        murow = Segment(length=3500, range=Range.objects.filter(name="Tatry")[0])
        murow.save()
        self.custom2 = CustomSegment(segment=murow, start_name="start_name", start_height=100, end_height=700,
                                     end_name="end_name", name="test4", elevation=1060)
        self.custom2.save()

    def test_empty_routes(self):
        points = CountPoints.count_all_points(self.routes)
        self.assertEqual(0, points)

    def test_routes_with_defined_segments(self):
        self.route1.segments.add(self.defined1.segment)
        self.route1.segments.add(self.defined2.segment)
        self.route2.segments.add(self.defined1.segment)
        points = CountPoints.count_all_points(self.routes)
        self.assertEqual(250, points)

    def test_routes_with_custom_segments(self):
        self.route1.segments.add(self.custom1.segment)
        self.route2.segments.add(self.custom1.segment)
        self.route2.segments.add(self.custom2.segment)
        points = CountPoints.count_all_points(self.routes)
        self.assertEqual(32, points)

    def test_routes_with_mix_segments(self):
        self.route1.segments.add(self.defined1.segment)
        self.route1.segments.add(self.defined2.segment)
        self.route2.segments.add(self.defined1.segment)
        self.route1.segments.add(self.custom1.segment)
        self.route2.segments.add(self.custom1.segment)
        self.route2.segments.add(self.custom2.segment)
        points = CountPoints.count_all_points(self.routes)
        self.assertEqual(282, points)
