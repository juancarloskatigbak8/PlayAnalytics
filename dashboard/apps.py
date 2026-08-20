# dashboard/apps.py

# Import the AppConfig base class from Django
from django.apps import AppConfig

# Define the configuration for the 'dashboard' app
class DashboardConfig(AppConfig):
    # Automatically use BigAutoField for primary keys by default
    default_auto_field = "django.db.models.BigAutoField"

    # Set the name of this app as 'dashboard'
    name = "dashboard"
