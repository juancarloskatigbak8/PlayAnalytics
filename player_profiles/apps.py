# Configuration for the player_profiles Django app
from django.apps import AppConfig


class PlayerProfilesConfig(AppConfig):
    # Default type for auto-generated primary keys in models
    default_auto_field = "django.db.models.BigAutoField"
    
    # The name of the app (must match the folder name)
    name = "player_profiles"
