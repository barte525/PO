from django.views import View
from django.shortcuts import render, redirect


class ProfileView(View):
    def get(self, request):
        if request.user.is_authenticated:
            name = request.user.name
            surname = request.user.surname
            return render(request, 'profile.html', {'name': name, 'surname': surname})
        else:
            return redirect('/login')
