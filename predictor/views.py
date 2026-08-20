from django.shortcuts import render, redirect
import pandas as pd
import joblib
from .forms import PlayerPredictionForm
from player_profiles.models import PlayerProfile
from .utils import get_most_common_risk_label
from django.contrib.auth.decorators import login_required

# ==============================
# Load the trained AI model and label encoder once on module import
# ==============================
model = joblib.load('predictor/rf_injury_model.joblib')
label_encoder = joblib.load('predictor/risk_label_encoder.joblib')

# ==============================
# Heuristic fallback function
# Used when the AI's prediction seems too optimistic
# ==============================
def assign_risk_label(player):
    # Calculate a performance load score
    perf_load = (
        player.games_played * player.minutes_played
        + player.field_goals_attempted
        + player.three_point_field_goals_attempted
        + player.free_throws_attempted
    )
    
    injuries = player.total_injuries
    injury_type = player.most_common_injury.lower()

    # Simple rules based on number of injuries and type
    if injuries <= 2 and injury_type in ["eye", "illness", "none"]:
        return "Low"
    elif 3 <= injuries <= 5 and perf_load < 10000:
        return "Low-Medium"
    elif 3 <= injuries <= 5 and perf_load >= 10000:
        return "Medium"
    elif 6 <= injuries <= 10 and perf_load >= 15000:
        return "Medium-High"
    elif injuries > 10 and perf_load >= 20000:
        return "High"

# ==============================
# Injury Risk Prediction View
# ==============================
@login_required
def predict_injury(request):
    if request.method == 'POST':
        form = PlayerPredictionForm(request.POST)
        
        if form.is_valid():
            player = form.save(commit=False)  # Don't save to DB yet

            # Step 1: Create a DataFrame with model input fields
            input_data = pd.DataFrame([{
                'Age': player.age,
                'Height_in_Inches': player.height_in_inches,
                'Weight_in_Pounds': player.weight_in_pounds,
                'Games_Played': player.games_played,
                'Minutes_Played': player.minutes_played,
                'Field_Goals_Attempted': player.field_goals_attempted,
                'Three_Point_Field_Goals_Attempted': player.three_point_field_goals_attempted,
                'Free_Throws_Attempted': player.free_throws_attempted,
                'Steals': player.steals,
                'Blocks': player.blocks,
                'Fouls': player.fouls,
            }], columns=[
                'Age', 'Height_in_Inches', 'Weight_in_Pounds', 'Games_Played', 'Minutes_Played',
                'Field_Goals_Attempted', 'Three_Point_Field_Goals_Attempted',
                'Free_Throws_Attempted', 'Steals', 'Blocks', 'Fouls'
            ])

            # Step 2: Use model to predict injury risk index, then decode it to label
            prediction_index = model.predict(input_data)[0]
            predicted_label = label_encoder.inverse_transform([prediction_index])[0]

            # Step 3: Apply fallback if model underestimates risk
            if predicted_label == "Low" and player.total_injuries > 10:
                predicted_label = assign_risk_label(player)

            # Step 4: Attach prediction label
            player.predicted_risk_label = predicted_label

            # Step 5: Temporarily store data in session to allow saving later
            request.session['temp_player_data'] = {
                'name': player.name,
                'age': player.age,
                'height_in_inches': player.height_in_inches,
                'weight_in_pounds': player.weight_in_pounds,
                'position': player.position,
                'games_played': player.games_played,
                'minutes_played': player.minutes_played,
                'field_goals_attempted': player.field_goals_attempted,
                'three_point_field_goals_attempted': player.three_point_field_goals_attempted,
                'free_throws_attempted': player.free_throws_attempted,
                'steals': player.steals,
                'blocks': player.blocks,
                'fouls': player.fouls,
                'total_injuries': player.total_injuries,
                'most_common_injury': player.most_common_injury,
                'predicted_risk_label': predicted_label,
            }

            # Step 6: Pass prediction and form back to template
            context = {
                'form': form,
                'predicted_risk': predicted_label,
                'most_common_risk': get_most_common_risk_label(),
                'show_results': True,
            }
            return render(request, 'predictor/predict.html', context)

    else:
        form = PlayerPredictionForm()

    return render(request, 'predictor/predict.html', {'form': form})

# ==============================
# Save predicted player to DB from session data
# ==============================
@login_required
def add_to_profile(request):
    data = request.session.get('temp_player_data')
    if data:
        PlayerProfile.objects.create(**data)
        del request.session['temp_player_data']  # Clean up session
    return redirect('player_profiles:profile_list')
