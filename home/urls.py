from django.contrib import admin
from django.urls import path
from home import views
from .views import CustomerListView, CustomerCreateView,CustomerDetailView, Next_of_kinListView

app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),

    path('customer_create', CustomerCreateView.as_view(), name='customer-create'),
    path('customer_list', CustomerListView.as_view(), name='customer-list'),
    path('customer_detail/<int:pk>', CustomerDetailView.as_view(), name='customer-detail'),

    path('next_of_kin/', Next_of_kinListView.as_view(), name='next-of-kin')
    # path('', views.home, name='home'),
    # path('', views.home, name='home'),

]
