# dashboard/templatetags/dashboard_extras.py

# Import Django's template system
from django import template

# Register this Python module as a custom template tag library
register = template.Library()

# Custom template filter to safely access dictionary values in templates
@register.filter
def get_item(dictionary, key):
    """
    Safely retrieves the value for the given key from a dictionary in a Django template.
    
    Usage in template:
      {{ my_dict|get_item:"some_key" }}

    If the key doesn't exist, it returns 0 instead of causing an error.
    This is useful when rendering charts or summaries with missing data.
    """
    return dictionary.get(key, 0)
