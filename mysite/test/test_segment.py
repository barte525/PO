from django.test import TestCase
from mysite.models.segment import DefinedSegment, Segment
from mysite.models.range import Range
from mysite.models.point import Point
import os
from mysite.views.segment import SegmentView

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'


class TestSegment(TestCase):
    def setUp(self):
        przelecz = Segment(length=1500, range=Range.objects.filter(name="Beskid Żywiecki")[0])
        przelecz.save()
        segment = DefinedSegment(segment=przelecz, points=100, name="test",
                                 start_point=Point.objects.filter(name="Murowaniec")[0],
                                 end_point=Point.objects.filter(name="Czarny staw")[0])
        segment.save()
        self.segment = DefinedSegment.objects.filter(name="test")

        przelecz = Segment(length=1500, range=Range.objects.filter(name="Beskid Żywiecki")[0])
        przelecz.save()
        segment = DefinedSegment(segment=przelecz, points=100, name="ex_test",
                                 start_point=Point.objects.filter(name="Murowaniec")[0],
                                 end_point=Point.objects.filter(name="Czarny staw")[0])
        segment.save()
        self.ex_segment = segment

    def test_incorrect_length_update(self):
        response = SegmentView.update_segment(self.segment, -1, 1, 1, 1, 1, "test")
        self.assertEqual(response, "Nie prawidłowa długość")
        self.assertEqual(self.segment[0], DefinedSegment.objects.get(name="test"))

    def test_incorrect_points_update(self):
        response = SegmentView.update_segment(self.segment, 1, 1, 1, 1, -1, "test")
        self.assertEqual(response, "Nie prawidłowa liczba punktów")
        self.assertEqual(self.segment[0], DefinedSegment.objects.get(name="test"))

    def test_incorrect_name_length(self):
        response = SegmentView.update_segment(self.segment, 1, 1, 1, 1, 1, "x" * 51)
        self.assertEqual(response, "Długość nazwy odcnika poza przedziałem <1,50>")
        self.assertEqual(self.segment[0], DefinedSegment.objects.get(name="test"))
        response = SegmentView.update_segment(self.segment, 1, 1, 1, 1, 1, "")
        self.assertEqual(response, "Długość nazwy odcnika poza przedziałem <1,50>")
        self.assertEqual(self.segment[0], DefinedSegment.objects.get(name="test"))

    def test_not_unique_name(self):
        response = SegmentView.update_segment(self.segment, 1, 1, 1, 1, 1, "ex_test")
        self.assertEqual(response, "Odcinek o podanej nazwie już istnieje")
        self.assertEqual(self.segment[0], DefinedSegment.objects.get(name="test"))

    def test_correct_update(self):
        response = SegmentView.update_segment(self.segment, 1, 1, 1, 1, 1, "new_test")
        self.assertEqual(response, "updated")
        self.assertEqual(DefinedSegment.objects.get(name="new_test").name, "new_test")
        self.assertEqual(list(DefinedSegment.objects.filter(name="test")), [])

