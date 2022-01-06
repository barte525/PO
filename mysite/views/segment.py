from django.views import View
from mysite.models.segment import DefinedSegment
from mysite.models.point import Point
from mysite.models.range import Range
from django.shortcuts import render


class SegmentView(View):

    def get(self, request, name):
        segment = DefinedSegment.objects.get(name=name)
        ranges = list(Range.objects.all())
        points = list(Point.objects.all())
        return render(request, 'defined_segment.html', {'segment': segment, 'ranges': ranges, 'points': points})