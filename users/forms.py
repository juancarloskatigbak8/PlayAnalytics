from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Custom registration form extending Django's built-in UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User  # Use Django's default User model
        fields = ['username', 'password1', 'password2']  # Only ask for username and password fields
