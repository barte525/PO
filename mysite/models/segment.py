from django.db import models
from .point import Point


class Segment(models.Model):
    length = models.IntegerField()
    name = models.CharField(max_length=100)
    #range = models.ForeignKey(User, on_delete=models.CASCADE)


class DefinedSegment(models.Model):
    segment = models.ForeignKey(Segment, on_delete=models.CASCADE)
    points = models.IntegerField()
    start_point = models.ForeignKey(Point, on_delete=models.PROTECT)
    end_point = models.ForeignKey(Point, on_delete=models.PROTECT)


class CustomSegment(models.Model):
    elevation = models.IntegerField()
    start_name = models.CharField(max_length=50)