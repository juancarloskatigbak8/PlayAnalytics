from player_profiles.models import PlayerProfile
from collections import Counter

# Utility function to get the most frequent risk level across all saved player profiles
def get_most_common_risk_label():
    # Extract all predicted_risk_label values from the PlayerProfile model
    risks = PlayerProfile.objects.values_list('predicted_risk_label', flat=True)

    # Count the frequency of each risk label using Python's Counter
    risk_counter = Counter(risks)

    # Return the most common risk label if available, else return None
    if risk_counter:
        return risk_counter.most_common(1)[0][0]
    return None
