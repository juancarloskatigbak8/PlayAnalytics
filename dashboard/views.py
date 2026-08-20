# Import necessary Django and Python modules
from django.shortcuts import render
from player_profiles.models import PlayerProfile  # Import the PlayerProfile model to access player data
from collections import defaultdict               # Used for grouping and initializing risk levels
from django.db.models import Avg, Count           # For calculating average values and counting entries
from django.contrib.auth.decorators import login_required  # To restrict access to authenticated users

# === LANDING PAGE VIEW ===
def landing_page(request):
    """
    This view simply renders the homepage (index.html).
    It's typically used for unauthenticated users or general visitors.
    """
    return render(request, 'index.html')

# === DASHBOARD VIEW ===
@login_required
def dashboard_view(request):
    """
    This view renders the main Dashboard page for logged-in users.
    It gathers and calculates statistics like average injuries, risk levels,
    and injury distributions to be visualized using Chart.js on the frontend.
    """

    # --- AVERAGE INJURIES BY POSITION ---
    # Group players by their position and calculate the average number of injuries per position
    avg_injuries = PlayerProfile.objects.values('position').annotate(avg=Avg('total_injuries'))
    injuries_by_position = {entry['position']: round(entry['avg'], 2) for entry in avg_injuries}

    # --- INJURY TYPE DISTRIBUTION ---
    # Count how many times each injury type appears
    injury_counts = PlayerProfile.objects.values('most_common_injury').annotate(count=Count('most_common_injury'))
    total_injuries = sum(entry['count'] for entry in injury_counts)  # Total number of injuries recorded

    # Calculate what percentage each injury type represents
    injuries_by_type = {
        entry['most_common_injury']: round((entry['count'] / total_injuries) * 100, 2)
        for entry in injury_counts if entry['most_common_injury']
    }

    # --- RISK LEVEL DISTRIBUTION BY POSITION ---
    risk_levels = ["High", "Medium-High", "Medium", "Low-Medium", "Low"]  # Ordered risk levels

    # Initialize a dictionary to count how many players per risk level for each position
    risk_raw = defaultdict(lambda: {level: 0 for level in risk_levels})
    for player in PlayerProfile.objects.all():
        risk = player.predicted_risk_label
        pos = player.position
        if risk in risk_levels:
            risk_raw[pos][risk] += 1  # Increment count for that risk level at that position

    # Format the data for Chart.js stacked bar chart
    positions = list(risk_raw.keys())
    risk_datasets = []
    for level in risk_levels:
        risk_datasets.append({
            'label': level,
            'data': [risk_raw[pos][level] for pos in positions],
            'stack': 'Stack'  # Group the bars together per position
        })

    # --- CONTEXT DATA FOR TEMPLATE ---
    # This dictionary is passed to the dashboard.html template
    context = {
        'injuries_by_position': injuries_by_position,
        'injuries_by_position_labels': list(injuries_by_position.keys()),
        'injuries_by_position_values': list(injuries_by_position.values()),

        'injury_type_labels': list(injuries_by_type.keys()),
        'injury_type_values': list(injuries_by_type.values()),

        'positions': positions,
        'risk_datasets': risk_datasets,

        'num_players': PlayerProfile.objects.count(),  # Total number of players
        'avg_age': round(PlayerProfile.objects.aggregate(avg=Avg("age"))["avg"] or 0, 1),  # Average player age
        'avg_injuries': round(PlayerProfile.objects.aggregate(avg=Avg("total_injuries"))["avg"] or 0, 2),  # Average injuries overall

        # Determine the most frequently occurring injury type
        'common_injury': PlayerProfile.objects.values("most_common_injury")
                            .annotate(count=Count("most_common_injury"))
                            .order_by("-count")
                            .first().get("most_common_injury", "None") if PlayerProfile.objects.exists() else "None",
    }

    # Render the dashboard.html template with the gathered context data
    return render(request, "dashboard/dashboard.html", context)
