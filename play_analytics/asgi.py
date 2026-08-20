"""
ASGI config for play_analytics project.

This file sets up the ASGI (Asynchronous Server Gateway Interface) application 
for the Django project. ASGI is the successor to WSGI and supports asynchronous
web protocols like WebSockets, making it more flexible for modern web apps.

It exposes the ASGI application as a module-level variable named ``application``,
which can be used by ASGI servers (like Daphne or Uvicorn) to run the app.

For more details:
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os  # Provides tools for interacting with the operating system

# Import Django's function to get the ASGI application
from django.core.asgi import get_asgi_application

# Set the default settings module for the Django project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'play_analytics.settings')

# Create the ASGI application callable
# This will be used by ASGI servers to serve your Django project
application = get_asgi_application()
