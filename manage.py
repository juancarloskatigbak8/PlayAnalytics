#!/usr/bin/env python
"""Django's command-line utility for administrative tasks like runserver, migrate, shell, etc."""

import os
import sys

def main():
    """
    Entry point for Django's command-line utility.
    Sets up the environment and runs management commands.
    """
    # Set default settings module for the Django project
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'play_analytics.settings')
    
    try:
        # Import the function that runs Django commands (e.g., runserver, migrate)
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Handle case where Django isn't installed or virtual environment isn't activated
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Run the command passed via CLI
    execute_from_command_line(sys.argv)

# If the script is run directly (not imported), call main()
if __name__ == '__main__':
    main()
