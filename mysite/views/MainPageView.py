from django.http import HttpResponse
from django.views import View
from mysite.services.insert_objects_to_database import insert_points_to_db
from mysite.models.point import Point


class MyView(View):
    def get(self, request):
        return HttpResponse('Nasz strona gówna')


class SavePoints(View):
    def get(self, request):
        insert_points_to_db()
        return HttpResponse('saved')


class GetPoints(View):
    def get(self, request):
        queryset = list(Point.objects.all())
        return HttpResponse(queryset)