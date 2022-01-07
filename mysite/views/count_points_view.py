from django.views import View
from django.shortcuts import render
from mysite.models.point import Point
from mysite.models.range import Range
from django.http import HttpResponse


class CountPoints(View):
    def get(self, request):
        return render(request, 'countpoints.html')

    def post(self, request):
        points =
        message_positive = "Gratulujemy zaangażowania i życzymy powodzenia w dalszym zdobywaniu szczytów!"
        message_zero = "Cieszymy się, że pragniesz zdobyć odznakę. \n Wprowadzaj przebyte trasy i podliczaj zdobyte punkty. Do dzieła!"

        if points > 0:
            message = message_positive
        else:
            message = message_zero

        return render(request, 'countpoints.html', {'points': points, 'message': message})