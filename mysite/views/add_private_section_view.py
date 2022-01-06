from django.views import View
from django.shortcuts import render
from mysite.models.point import Point
from mysite.models.range import Range
from django.http import HttpResponse
from mysite.models.segment import CustomSegment, Segment
from mysite.models.point import Point
from mysite.models.range import Range


class AddPrivateSection(View):
    def get(self, request):
        ranges = list(Range.objects.all())
        points = list(Point.objects.all())
        return render(request, 'addprivatesection.html', {'ranges': ranges, 'points': points})

    def post(self, request):
        length = request.POST.get("input_length")
        range_id = request.POST.get("select_mountain_range")
        range = Range.objects.get(id=range_id)
        segment = Segment(length=length, range=range)
        segment.save()
        if request.POST.get("point_type_s") == "defined_point_s":
            start_point = Point.objects.get(id=request.POST.get("select_start_point"))
            start_height = start_point.height
            start_name = start_point.name
        else:
            start_height = request.POST.get("input_s_point_height")
            start_name = request.POST.get("input_s_point_name")
        if request.POST.get("point_type_e") == "defined_point_e":
            end_point = Point.objects.get(id=request.POST.get("select_end_point"))
            end_height = end_point.height
            end_name = end_point.name
        else:
            end_height = request.POST.get("input_e_point_height")
            end_name = request.POST.get("input_e_point_name")
        name = request.POST.get("input_name")
        elevation = request.POST.get("input_elevation_gain")
        CustomSegment(segment=segment, start_name=start_name, start_height=start_height, end_height=end_height,
                      end_name=end_name, name=name, elevation=elevation).save()
        return HttpResponse("Ok")