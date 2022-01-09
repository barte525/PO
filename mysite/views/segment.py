from django.views import View
from mysite.models.segment import DefinedSegment, Segment
from mysite.models.point import Point
from mysite.models.range import Range
from django.shortcuts import render
from django.http import HttpResponse
from mysite.services.responses import get_error_message


class SegmentView(View):

    def get(self, request, name):
        try:
            segment = DefinedSegment.objects.get(name=name)
        except Exception:
            return HttpResponse(get_error_message("Nie znaleziono odcinka o podanej nazwie."))
        ranges = list(Range.objects.all())
        points = list(Point.objects.all())
        return render(request, 'defined_segment.html', {'segment': segment, 'ranges': ranges, 'points': points})

    def post(self, request, name):
        current_segment = DefinedSegment.objects.filter(name=name)
        if "update" in request.POST:
            end_point = request.POST.get("select_end_point", "")
            start_point = request.POST.get("select_start_point", "")
            range = request.POST.get("select_mountain_range")
            length = request.POST.get("length", "")
            if int(length) <= 0:
                return HttpResponse(get_error_message("Nie prawidłowa długość"))
            points = request.POST.get("points", "")
            if int(points) <= 0:
                return HttpResponse(get_error_message("Nie prawidłowa liczba punktów"))
            name = request.POST.get("name", "")
            if len(name) < 1 or len(name) > 50:
                return HttpResponse(get_error_message("Długość nazwy odcnika poza przedziałem <1,50>"))
            if DefinedSegment.objects.filter(name=name).exists():
                return HttpResponse(get_error_message("Odcinek o podanej nazwie już istnieje"))
            segment = Segment.objects.filter(id=current_segment[0].segment.id)
            segment.update(range=range, length=length)
            current_segment.update(end_point=end_point, start_point=start_point, points=points, name=name, segment=segment[0])
            return HttpResponse("updated")
        if "delete" in request.POST:
            current_segment[0].delete()
            return HttpResponse("deleted")
