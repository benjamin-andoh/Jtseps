from django.contrib import admin
from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    path('', views.home, name='home'),
]