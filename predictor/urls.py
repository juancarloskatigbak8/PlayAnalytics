from django.urls import path
from . import views

# This sets the app namespace for URL reversing in templates: {% url 'predictor:predict_injury' %}
app_name = 'predictor'

urlpatterns = [
    # Route to display the prediction form and handle model-based prediction logic
    path('predict/', views.predict_injury, name='predict_injury'),

    # Route to save the predicted player to the profile after a prediction
    path('add-to-profile/', views.add_to_profile, name='add_to_profile'), 
]
