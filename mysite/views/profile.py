from django.views import View
from django.shortcuts import render, redirect
from mysite.models.user import User


class ProfileView(View):
    def get(self, request):
        print("to" + str(request.user.id))
        if User.objects.filter(id=request.user.id).exists():
            name = request.user.name
            surname = request.user.surname
            return render(request, 'profile.html', {'name': name, 'surname': surname})
        else:
            return redirect('/login')
