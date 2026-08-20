# dashboard/urls.py

# Import Django's path function to define URL patterns
from django.urls import path

# Import views from the current app (dashboard/views.py)
from . import views

# Set the namespace for this app's URLs, useful when referencing URLs in templates using {% url 'dashboard:dashboard_view' %}
app_name = 'dashboard'

# Define URL patterns for the dashboard app
urlpatterns = [
    # Map the root URL of the dashboard app (e.g., /dashboard/) to the dashboard_view function
    path('', views.dashboard_view, name='dashboard_view'),
]
