from django.contrib import admin
from django.urls import path
from home import views
from .views import CustomerListView, CustomerCreateView

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),

    path('customer_create', CustomerCreateView.as_view(), name='customer-create'),
    path('customer_list', CustomerListView.as_view(), name='customer-list'),
    # path('', views.home, name='home'),
    # path('', views.home, name='home'),
    # path('', views.home, name='home'),

]
