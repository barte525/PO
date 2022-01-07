"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mysite.views.MainPageView import MyView, SavePoints, GetPoints
from mysite.views.add_private_section_view import AddPrivateSection
from mysite.views.count_points_view import CountPoints
from django.contrib.auth import views as auth_views
from mysite.views.profile import ProfileView
from mysite.views.segment import SegmentView
from mysite.views.view_segments_view import ViewSegments

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MyView.as_view()),
    path('save/', SavePoints.as_view()),
    path('get/', GetPoints.as_view()),
    path('login/', auth_views.LoginView.as_view(template_name="login.html")),
    path('add_private_section/', AddPrivateSection.as_view()),
    path('count_points/<int:id>', CountPoints.as_view()),
    path('view_segments/', ViewSegments.as_view()),
    path('profile/', ProfileView.as_view()),
    path('section/<str:name>', SegmentView.as_view())
]
