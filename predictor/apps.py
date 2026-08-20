from django.apps import AppConfig

# Configuration class for the 'predictor' app.
# Django uses this to initialize and configure the app.
class PredictorConfig(AppConfig):
    # Sets the default primary key type to BigAutoField (a 64-bit integer).
    default_auto_field = "django.db.models.BigAutoField"

    # Name of the app (used for Django's internal app registry).
    name = "predictor"
