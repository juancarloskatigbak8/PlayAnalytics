"""
WSGI config for the PlayAnalytics project.

This file exposes the WSGI callable as a module-level variable named `application`.

WSGI (Web Server Gateway Interface) is used for deploying Django apps on production servers.
For more info: https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Set the default Django settings module for the 'wsgi' command
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'play_analytics.settings')

# Get the WSGI application callable to be used by WSGI servers like Gunicorn
application = get_wsgi_application()
