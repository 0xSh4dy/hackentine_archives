"""chall_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import re_path, include
from django.http import HttpResponse, HttpRequest
import os

FLAG = os.getenv("FLAG")
ADMIN_TOKEN = os.getenv("ADMIN_TOKEN")

def flag(request: HttpRequest):
    token = request.COOKIES.get('token')
    print(token,ADMIN_TOKEN)
    if not token or token != ADMIN_TOKEN:
        return HttpResponse("You are not admin")
    return HttpResponse(FLAG)

def index(request: HttpRequest):
    return HttpResponse("I am a simple web app. I have a flag. But I don't want to give it to you.")

urlpatterns = [
    re_path('index', index),
    re_path('flag', flag),
]
