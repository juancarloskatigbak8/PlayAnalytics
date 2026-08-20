from django.db import models

# This file is intentionally left blank because the predictor app
# does not require its own database models.

# All player data is managed through the PlayerProfile model
# in the `player_profiles` app, which this app imports and uses.

# You may safely leave this file as-is unless the predictor app
# eventually needs to store its own data (e.g., prediction logs or history).
