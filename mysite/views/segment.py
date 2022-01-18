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
            name_i = request.POST.get("name", "")
            messege = self.update_segment(current_segment, length, end_point, start_point, range, points, name_i, name)
            return HttpResponse(get_error_message(messege))
        if "delete" in request.POST:
            current_segment[0].delete()
            return HttpResponse("usunieto")

    @staticmethod
    def update_segment(current_segment, length, end_point, start_point, range, points, name_i, name):
        if int(length) <= 0:
            return "Nieprawidłowa długość"
        if int(points) <= 0:
            return "Nieprawidłowa liczba punktów"
        if len(name_i) < 1 or len(name_i) > 50:
            return "Długość nazwy odcinka poza przedziałem <1,50>"
        if DefinedSegment.objects.filter(name=name_i).exists() and name_i != name:
            return "Odcinek o podanej nazwie już istnieje"
        segment = Segment.objects.filter(id=current_segment[0].segment.id)
        segment.update(range=range, length=length)
        current_segment.update(end_point=end_point, start_point=start_point, points=points, name=name,
                               segment=segment[0])
        return "zaktualizowano"
