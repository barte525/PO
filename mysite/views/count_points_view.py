from django.views import View
from django.shortcuts import render
from mysite.models.point import Point
from mysite.models.range import Range
from mysite.models.route import Route
from mysite.models.segment import Segment, DefinedSegment, CustomSegment
from mysite.models.user import User, Tourist
from django.http import HttpResponse


class CountPoints(View):
    def get(self, request, id):
        return render(request, 'countpoints.html')

    def post(self, request, id):
        if not User.objects.filter(id=id).exists():
            return HttpResponse("Błędne dane (id)")

        user = User.objects.get(id=id)
        tourist = Tourist.objects.get(user=user)
        routes = list(Route.objects.filter(tourist=tourist))
        points = 0

        for route in routes:
            segments = route.segments.all()
            c_segment_points = 0
            for segment in segments:
                if DefinedSegment.objects.filter(segment=segment.id).exists():
                    points += DefinedSegment.objects.get(segment=segment.id).points
                else:
                    elevation_gain = CustomSegment.objects.get(segment=segment.id).elevation
                    length = Segment.objects.get(id=segment.id).length
                    c_segment_points += self.count_points(elevation_gain, length)

            if c_segment_points > 50:
                c_segment_points = 50

            points += c_segment_points

        message_positive = "Gratulujemy zaangażowania i życzymy powodzenia w dalszym zdobywaniu szczytów!"
        message_zero = "Cieszymy się, że pragniesz zdobyć odznakę. \n Wprowadzaj przebyte trasy i podliczaj zdobyte punkty. Do dzieła!"

        if points > 0:
            message = message_positive
        else:
            message = message_zero

        return render(request, 'countpoints.html', {'points': points, 'message': message})

    def count_points(self, elevation_gain, length):
        elevation_gain_points = elevation_gain // 100
        length_points = length // 1000

        if elevation_gain % 100 > 50:
            elevation_gain_points += 1
        if length % 1000 > 500:
            length_points += 1

        points = elevation_gain_points + length_points
        return points
