from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views

app_name = "users"
urlpatterns = [
    path('register/', user_views.register_page, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]