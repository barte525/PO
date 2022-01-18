from django.views import View
from django.shortcuts import render
from mysite.models.route import Route
from mysite.models.segment import Segment, DefinedSegment, CustomSegment
from mysite.models.user import Tourist
from django.http import HttpResponse


class CountPoints(View):
    def get(self, request):
        return render(request, 'countpoints.html')

    def post(self, request):
        print(request.user.id)
        if not Tourist.objects.filter(user=request.user.id).exists():
            return HttpResponse("Uzytkownik nie jest turystą")

        tourist = Tourist.objects.get(user=request.user.id)
        routes = list(Route.objects.filter(tourist=tourist))

        points = self.count_all_points(routes)

        message_positive = "Gratulujemy zaangażowania i życzymy powodzenia w dalszym zdobywaniu szczytów!"
        message_zero = "Cieszymy się, że pragniesz zdobyć odznakę. \n Wprowadzaj przebyte trasy i podliczaj zdobyte punkty. Do dzieła!"

        if points > 0:
            message = message_positive
        else:
            message = message_zero

        return render(request, 'countpoints.html', {'points': points, 'message': message})

    @staticmethod
    def count_all_points(routes):
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
                    c_segment_points += CountPoints.count_points(elevation_gain, length)

            if c_segment_points > 50:
                c_segment_points = 50

            points += c_segment_points
        return points

    @staticmethod
    def count_points(elevation_gain, length):
        elevation_gain_points = elevation_gain // 100
        length_points = length // 1000

        if elevation_gain % 100 > 50:
            elevation_gain_points += 1
        if length % 1000 > 500:
            length_points += 1

        points = elevation_gain_points + length_points
        return points
