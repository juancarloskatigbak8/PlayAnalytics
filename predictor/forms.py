from django import forms
from player_profiles.models import PlayerProfile

# This form is used to input player statistics and generate an injury risk prediction.
# It is based on the PlayerProfile model.
class PlayerPredictionForm(forms.ModelForm):
    class Meta:
        model = PlayerProfile  # Links the form to the PlayerProfile model
        fields = [
            'name',                            # Player's name
            'age',                             # Player's age
            'height_in_inches',                # Height in inches
            'weight_in_pounds',                # Weight in pounds
            'position',                        # Player position (Guard, Forward, Center)
            'games_played',                    # Total number of games played
            'minutes_played',                  # Average minutes per game
            'field_goals_attempted',           # Total field goals attempted
            'three_point_field_goals_attempted', # Total 3-point field goals attempted
            'free_throws_attempted',           # Total free throws attempted
            'steals',                          # Total steals
            'blocks',                          # Total blocks
            'fouls',                           # Total fouls
            'total_injuries',                  # Total recorded injuries
            'most_common_injury',              # Most frequently occurring injury
        ]
