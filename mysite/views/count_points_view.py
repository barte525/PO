from django.views import View
from django.shortcuts import render
from mysite.models.point import Point
from mysite.models.range import Range
from mysite.models.route import Route
from mysite.models.user import User, Tourist
from django.http import HttpResponse


class CountPoints(View):
    def get(self, request):
        return render(request, 'countpoints.html')

    def post(self, request):
        user = User.objects.get(id=id)
        tourist = Tourist.objects.get(user=user)
        routes = Route.objects.get(tourist=tourist)
        for route in routes:
            points = 1

        message_positive = "Gratulujemy zaangażowania i życzymy powodzenia w dalszym zdobywaniu szczytów!"
        message_zero = "Cieszymy się, że pragniesz zdobyć odznakę. \n Wprowadzaj przebyte trasy i podliczaj zdobyte punkty. Do dzieła!"

        if points > 0:
            message = message_positive
        else:
            message = message_zero

        return render(request, 'countpoints.html', {'points': points, 'message': message})