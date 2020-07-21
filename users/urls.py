from django.urls import path
from users import views as user_views

app_name = "users"
urlpatterns = [
    path('register/', user_views.register_page, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', user_views.login_page, name='login'),
    path('logout/', user_views.logout_page , name='logout'),

    path('employee_list', user_views.list_employee, name='employee-list')
]