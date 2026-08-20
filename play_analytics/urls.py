"""
URL configuration for the PlayAnalytics project.

This file defines how URLs are routed to views.
Docs: https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from dashboard.views import landing_page, dashboard_view
from django.conf import settings
from django.conf.urls.static import static

# === Main URL Patterns ===
urlpatterns = [
    path('admin/', admin.site.urls),                     # Admin panel
    path('profiles/', include('player_profiles.urls')),  # Player profile routes
    path('predictor/', include('predictor.urls')),       # Injury prediction routes
    path('dashboard/', include('dashboard.urls')),       # Dashboard app routes
    path('users/', include('users.urls')),               # Login/register/logout URLs

    path('', landing_page, name='landing'),              # Home page view (index.html)


]

# === Serve media files in development mode ===
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
