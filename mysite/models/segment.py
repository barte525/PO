from django.db import models
from .point import Point
from .range import Range


class Segment(models.Model):
    length = models.IntegerField()
    name = models.CharField(max_length=100)
    range = models.ForeignKey(Range, on_delete=models.CASCADE, null=True)


class DefinedSegment(models.Model):
    segment = models.ForeignKey(Segment, on_delete=models.CASCADE)
    points = models.IntegerField()
    start_point = models.ForeignKey(Point, on_delete=models.PROTECT, related_name='start_point')
    end_point = models.ForeignKey(Point, on_delete=models.PROTECT, related_name='end_point')


class CustomSegment(models.Model):
    elevation = models.IntegerField()
    start_name = models.CharField(max_length=50)
    end_name = models.CharField(max_length=50)
    start_height = models.IntegerField()
    end_height = models.IntegerField()
    segment = models.ForeignKey(Segment, on_delete=models.CASCADE)
