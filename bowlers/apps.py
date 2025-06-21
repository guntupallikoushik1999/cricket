from django.apps import AppConfig

"""
BowlersConfig is the configuration class for the 'bowlers' app in a Django project.
It sets the default auto field type and specifies the name of the app.
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator"""
class BowlersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bowlers'
