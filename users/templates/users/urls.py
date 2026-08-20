from django.urls import path
from . import views

# URL configuration for user authentication (register, login, logout)
urlpatterns = [
    # Route for user registration page
    path('register/', views.register_view, name='register'),

    # Route for user login page
    path('login/', views.login_view, name='login'),

    # Route for logging out the user
    path('logout/', views.logout_view, name='logout'),
]
