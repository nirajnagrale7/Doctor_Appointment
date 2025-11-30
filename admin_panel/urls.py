from django.urls import path
from . import views
from django.contrib.auth import views as auth_views # Import Django's built-in auth views

urlpatterns = [
    path('register/', views.admin_register, name='register'),
    path('login/', views.admin_login, name='login'),
    path('logout/', views.custom_logout_view, name='logout'), # Changed this line
    path('dashboard/', views.dashboard, name='dashboard'), # Dashboard URL
    path('profile/', views.profile, name='profile'), # Profile URL
    path('password_change/', views.change_password, name='change_password'), # Change password URL
]