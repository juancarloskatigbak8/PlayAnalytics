from django.db import models

# ==============================
# Player Profile Model
# ==============================
class PlayerProfile(models.Model):
    # Dropdown choices for player position
    POSITION_CHOICES = [
        ('Guard', 'Guard'),
        ('Forward', 'Forward'),
        ('Center', 'Center'),
    ]

    # Dropdown choices for most common injuries
    INJURY_CHOICES = [
        ('None', 'None'),
        ('Ankle', 'Ankle'),
        ('Pectoral', 'Pectoral'),
        ('Toe', 'Toe'),
        ('Back', 'Back'),
        ('Knee', 'Knee'),
        ('Finger', 'Finger'),
        ('Hamstring', 'Hamstring'),
        ('Groin', 'Groin'),
        ('Nose', 'Nose'),
        ('Wrist', 'Wrist'),
        ('Illnesses', 'Illnesses'),
        ('Thoracic', 'Thoracic'),
        ('Abdominal', 'Abdominal'),
        ('Adductor', 'Adductor'),
        ('Foot', 'Foot'),
        ('Calf', 'Calf'),
        ('Shoulder', 'Shoulder'),
        ('Hip', 'Hip'),
        ('Concussions', 'Concussions'),
        ('Neck', 'Neck'),
        ('Mouth', 'Mouth'),
        ('Quadriceps', 'Quadriceps'),
        ('Elbow', 'Elbow'),
        ('Achilles', 'Achilles'),
        ('Oblique', 'Oblique'),
        ('Eye', 'Eye')
    ]

    # Basic player information
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    height_in_inches = models.FloatField()
    weight_in_pounds = models.FloatField()
    position = models.CharField(max_length=50, choices=POSITION_CHOICES)

    # Performance stats
    games_played = models.IntegerField()
    minutes_played = models.FloatField()
    field_goals_attempted = models.IntegerField()
    three_point_field_goals_attempted = models.IntegerField()
    free_throws_attempted = models.IntegerField()
    steals = models.IntegerField()
    blocks = models.IntegerField()
    fouls = models.IntegerField()

    # Injury-related stats
    predicted_risk_label = models.CharField(max_length=50, blank=True, null=True)  # Output from AI model
    total_injuries = models.IntegerField(default=0)
    most_common_injury = models.CharField(
        max_length=100,
        choices=INJURY_CHOICES,
        blank=True,
        null=True
    )

    # Optional player profile image
    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


# ==============================
# Player Notes Model
# ==============================
class PlayerNotes(models.Model):
    # Each note is linked to a specific player profile
    player = models.ForeignKey(
        PlayerProfile,
        on_delete=models.CASCADE,
        related_name='notes'
    )
    text = models.TextField()  # Content of the note
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when note was added

    def __str__(self):
        return f"Note for {self.player.name} on {self.created_at.strftime('%Y-%m-%d')}"
