from django.views import View
from django.shortcuts import render
from mysite.models.point import Point
from mysite.models.range import Range
from django.http import HttpResponse


class AddPrivateSection(View):
    def get(self, request):
        ranges = list(Range.objects.all())
        points = list(Point.objects.all())
        return render(request, 'addprivatesection.html', {'ranges': ranges, 'points': points})

    def post(self, request):

        return HttpResponse("Ok")