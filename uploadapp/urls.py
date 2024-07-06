from http.client import HTTPResponse
from django.http import HttpResponse
from django.contrib import admin
from django.urls import path,include
from . import views




urlpatterns = [
    
    path('image', views.upload_addimage, name="imageupload" ),
]
    