from django.views import View
from mysite.models.segment import DefinedSegment, Segment
from mysite.models.point import Point
from mysite.models.range import Range
from django.shortcuts import render
from django.http import HttpResponse


class SegmentView(View):

    def get(self, request, name):
        segment = DefinedSegment.objects.get(name=name)
        ranges = list(Range.objects.all())
        points = list(Point.objects.all())
        return render(request, 'defined_segment.html', {'segment': segment, 'ranges': ranges, 'points': points})

    def post(self, request, name):
        current_segment = DefinedSegment.objects.filter(name=name)
        if "update" in request.POST:
            current_segment = DefinedSegment.objects.filter(name=name)
            end_point = request.POST.get("select_end_point", "")
            start_point = request.POST.get("select_start_point", "")
            range = request.POST.get("select_mountain_range")
            length = request.POST.get("length", "")
            points = request.POST.get("points", "")
            name = request.POST.get("name", "")
            segment = Segment.objects.filter(id=current_segment[0].segment.id)
            segment.update(range=range, length=length)
            current_segment.update(end_point=end_point, start_point=start_point, points=points, name=name)
            return HttpResponse("updated")
        if "delete" in request.POST:
            current_segment[0].delete()
            return HttpResponse("deleted")