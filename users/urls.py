from django.urls import path
from . import views

# URL patterns for user authentication system
urlpatterns = [
    # Login page
    path('login/', views.login_view, name='login'),

    # Logout (ends user session)
    path('logout/', views.logout_view, name='logout'),

    # Registration page
    path('register/', views.register_view, name='register'),
]
