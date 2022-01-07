from django.views import View
from django.shortcuts import render
from mysite.models.point import Point
from mysite.models.range import Range
from django.http import HttpResponse
from mysite.models.segment import CustomSegment, Segment
from mysite.models.point import Point
from mysite.models.range import Range
from mysite.models.route import Route


class AddPrivateSection(View):
    def get(self, request, id):
        ranges = list(Range.objects.all())
        points = list(Point.objects.all())
        return render(request, 'addprivatesection.html', {'ranges': ranges, 'points': points})

    def post(self, request, id):
        msg_valid_point_name = "Długość nazwy punktu nie może być mmniejsza od 1 znaku i większa od 200 znaków."
        msg_valid_segment_name = "Długość nazwy odcinka nie może być mmniejsza od 1 znaku i większa od 200 znaków."
        msg_valid_number = "Wprowadzona wartość liczbowa nie spełnia wymagań."

        length = request.POST.get("input_length")
        range_id = request.POST.get("select_mountain_range")
        range = Range.objects.get(id=range_id)
        segment = Segment(length=length, range=range)
        segment.save()
        if request.POST.get("point_type_s") == "defined_point_s":
            select_s_point = request.POST.get("select_start_point")
            start_point = Point.objects.get(id=select_s_point)
            start_height = start_point.height
            start_name = start_point.name
        else:
            start_height = request.POST.get("input_s_point_height")
            if (not (start_height.is_numeric() and start_height >= 0)):
                return HttpResponse(msg_valid_number)

            start_name = request.POST.get("input_s_point_name")
            start_name_length = len(start_name)
            if (start_name_length > 50 or start_name_length < 1):
                return HttpResponse(msg_valid_point_name)

        if request.POST.get("point_type_e") == "defined_point_e":
            select_e_point = request.POST.get("select_end_point")
            end_point = Point.objects.get(id=select_e_point)
            end_height = end_point.height
            end_name = end_point.name
        else:
            end_height = request.POST.get("input_e_point_height")
            if (not (end_height.is_numeric() and end_height >= 0)):
                return HttpResponse(msg_valid_number)

            end_name = request.POST.get("input_e_point_name")
            end_name_length = len(end_name)
            if (end_name_length > 50 or end_name_length < 1):
                return HttpResponse(msg_valid_point_name)

        name = request.POST.get("input_name")
        name_length = len(name)
        if (name_length > 100 or name_length < 1):
            return HttpResponse(msg_valid_segment_name)


        elevation = request.POST.get("input_elevation_gain")

        CustomSegment(segment=segment, start_name=start_name, start_height=start_height, end_height=end_height,
                      end_name=end_name, name=name, elevation=elevation).save()
        Route.objects.get(id=id).segments.add(segment)
        return HttpResponse("Odcinek został zapisany w bazie.")