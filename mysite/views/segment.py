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
            length = request.POST.get("length", "")
            end_point = request.POST.get("select_end_point", "")
            start_point = request.POST.get("select_start_point", "")
            range = request.POST.get("select_mountain_range", "")
            points = request.POST.get("points", "")
            name = request.POST.get("name", "")
            messege = self.update_segment(current_segment, length, end_point, start_point, range, points, name)
            return HttpResponse(get_error_message(messege))
        if "delete" in request.POST:
            current_segment[0].delete()
            return HttpResponse("deleted")

    @staticmethod
    def update_segment(current_segment, length, end_point, start_point, range, points, name):
        if int(length) <= 0:
            return "Nie prawidłowa długość"
        if int(points) <= 0:
            return "Nie prawidłowa liczba punktów"
        if len(name) < 1 or len(name) > 50:
            return "Długość nazwy odcnika poza przedziałem <1,50>"

        if DefinedSegment.objects.filter(name=name).exists():
            return "Odcinek o podanej nazwie już istnieje"
        segment = Segment.objects.filter(id=current_segment[0].segment.id)
        segment.update(range=range, length=length)
        current_segment.update(end_point=end_point, start_point=start_point, points=points, name=name,
                               segment=segment[0])
        return "updated"
