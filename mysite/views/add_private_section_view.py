from django.views import View
from django.shortcuts import render
from mysite.models.segment import CustomSegment, Segment
from mysite.models.point import Point
from mysite.models.range import Range
from mysite.models.route import Route
from django.http import HttpResponse


class AddPrivateSection(View):
    def get(self, request, id):
        ranges = list(Range.objects.all())
        points = list(Point.objects.all())
        return render(request, 'addprivatesection.html', {'ranges': ranges, 'points': points})

    def post(self, request, id):
        length = request.POST.get("input_length")
        range_id = request.POST.get("select_mountain_range")
        point_type_s = request.POST.get("point_type_s")
        select_s_point = request.POST.get("select_start_point")
        start_height = request.POST.get("input_s_point_height")
        start_name = request.POST.get("input_s_point_name")
        end_height = request.POST.get("input_e_point_height")
        end_name = request.POST.get("input_e_point_name")
        name = request.POST.get("input_name")
        point_type_e = request.POST.get("point_type_e")
        elevation = request.POST.get("input_elevation_gain")
        select_e_point = request.POST.get("select_end_point")
        return HttpResponse(self.create_segment(id, length, range_id, point_type_s, select_s_point, start_height, start_name,
                                end_height, end_name, name, point_type_e, elevation, select_e_point))

    @staticmethod
    def create_segment(id, length, range_id, point_type_s, select_s_point, start_height, start_name,
                       end_height, end_name, name, point_type_e, elevation, select_e_point):
        msg_valid_point_name = "Długość nazwy punktu nie może być mniejsza od 1 znaku i większa od 200 znaków."
        msg_valid_segment_name = "Długość nazwy odcinka nie może być mmniejsza od 1 znaku i większa od 200 znaków."
        msg_valid_point_height = "Wysokość n.p.m. punktu musi być liczbą większą lub równą 0."

        name_length = len(name)
        if name_length > 100 or name_length < 1:
            return msg_valid_segment_name
        if point_type_s == "defined_point_s":
            start_point = Point.objects.get(id=select_s_point)
            start_height = start_point.height
            start_name = start_point.name
        else:
            start_name_length = len(start_name)
            if start_name_length > 50 or start_name_length < 1:
                return msg_valid_point_name
            if not (start_height.isnumeric() and int(start_height) >= 0):
                return msg_valid_point_height
        if point_type_e == "defined_point_e":
            end_point = Point.objects.get(id=select_e_point)
            end_height = end_point.height
            end_name = end_point.name
        else:
            end_name_length = len(end_name)
            if end_name_length > 50 or end_name_length < 1:
                return msg_valid_point_name
            if not (end_height.isnumeric() and int(end_height) >= 0):
                return msg_valid_point_height

        range = Range.objects.get(id=range_id)
        segment = Segment(length=length, range=range)
        segment.save()

        CustomSegment(segment=segment, start_name=start_name, start_height=start_height, end_height=end_height,
                      end_name=end_name, name=name, elevation=elevation).save()
        Route.objects.get(id=id).segments.add(segment)
        return "Odcinek o naziwe " + name + " został zapisany w bazie."
