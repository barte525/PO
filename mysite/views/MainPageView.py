from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from mysite.models.point import Point


class MyView(View):
    def get(self, request):
        return HttpResponse('Nasz strona')


class SavePoints(View):
    def get(self, request):
        point = Point.objects.all()[0]
        return render(request, 'login.html', {'point': point})


class GetPoints(View):
    def get(self, request):
        queryset = Point.objects.values_list('name')
        return HttpResponse(queryset)
