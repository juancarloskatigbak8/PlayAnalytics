from django import forms
from .models import PlayerProfile, PlayerNotes

# === Form to handle player profile creation and editing ===
class PlayerProfileForm(forms.ModelForm):
    class Meta:
        model = PlayerProfile  # Bind this form to the PlayerProfile model
        fields = [
            'name', 'age', 'height_in_inches', 'weight_in_pounds', 'position',
            'games_played', 'minutes_played', 'field_goals_attempted',
            'three_point_field_goals_attempted', 'free_throws_attempted',
            'steals', 'blocks', 'fouls', 'predicted_risk_label',
            'total_injuries', 'most_common_injury', 'profile_picture'
        ]
        widgets = {
            # Dropdown for predefined positions (e.g., Guard, Forward, Center)
            'position': forms.Select(choices=PlayerProfile.POSITION_CHOICES),

            # Dropdown for predefined injury types
            'most_common_injury': forms.Select(choices=PlayerProfile.INJURY_CHOICES),

            # Style the file input for uploading profile pictures
            'profile_picture': forms.FileInput(attrs={
                'class': 'form-control',
            })
        }

    def __init__(self, *args, **kwargs):
        super(PlayerProfileForm, self).__init__(*args, **kwargs)
        # Set a friendly label for the image field
        self.fields['profile_picture'].label = "Change picture"

# === Form for adding a new note to a player's profile ===
class PlayerNoteForm(forms.ModelForm):
    class Meta:
        model = PlayerNotes  # Use the PlayerNotes model
        fields = ['text']    # Only one field: the content of the note

