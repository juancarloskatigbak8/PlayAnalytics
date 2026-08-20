from django.urls import path
from . import views

# Namespace for reverse URL resolution (e.g., 'player_profiles:add_player')
app_name = 'player_profiles'

# URL patterns for player profile features
urlpatterns = [
    # Home/index route (can be used for testing or landing page)
    path('', views.index, name='index'),

    # List view of all player profiles
    path('profiles/', views.profile_list, name='profile_list'),

    # Form to add a new player profile
    path('profiles/add/', views.add_player, name='add_player'),

    # Form to edit an existing player's profile
    path('profiles/<int:player_id>/edit/', views.edit_player, name='edit_player'),

    # Detail view of a single player's profile
    path('profiles/<int:pk>/', views.profile_detail, name='profile_detail'),

    # Form to add a note to a specific player
    path('profiles/<int:pk>/add_note/', views.add_note, name='add_note'),

    # Delete a specific player profile
    path('profiles/<int:pk>/delete/', views.delete_player, name='delete_player'),

    # Delete a specific note
    path('notes/<int:note_id>/delete/', views.delete_note, name='delete_note'),

    # Edit a specific note
    path('notes/<int:note_id>/edit/', views.edit_note, name='edit_note'),
]
