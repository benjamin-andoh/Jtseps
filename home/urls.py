from django.contrib import admin
from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
]