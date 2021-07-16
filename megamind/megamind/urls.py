"""megamind URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='Home'),
    path('about/', views.about, name='About'),
    path('contact/', views.contact, name='Contact'),
    path('courses/', views.courses, name='Courses'),
    path('events/', views.events, name='Events'),
    path('course-details/', views.course_details, name='Course-details'),
    path('pricing/', views.pricing, name='Pricing'),
    path('trainers/', views.trainers, name='Trainers'),
    path('abacus-d/', views.abacus_d, name='Trainers'),
]