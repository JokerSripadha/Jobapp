from http.client import HTTPResponse
from django.http import HttpResponse
from django.contrib import admin
from django.urls import path,include
from . import views




urlpatterns = [
    path('subscribe/', views.subscribe, name='subscribe'),
    path('thank-you/',views.thankyou,name='thankyou'),
    
]
