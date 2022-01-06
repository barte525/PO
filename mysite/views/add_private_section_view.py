from django.views import View
from django.shortcuts import render


class AddPrivateSection(View):
    def get(self, request):
        return render(request, 'addprivatesection.html')