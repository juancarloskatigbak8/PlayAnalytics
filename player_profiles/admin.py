# Django admin site configuration for the player_profiles app
from django.contrib import admin

# Import models defined in this app
from .models import PlayerProfile, PlayerNotes

# Register PlayerProfile model to appear in Django admin
admin.site.register(PlayerProfile)

# Register PlayerNotes model to appear in Django admin
admin.site.register(PlayerNotes)
