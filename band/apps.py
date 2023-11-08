from django.apps import AppConfig

class BandConfig(AppConfig):
    """
    This class represents the configuration for the band app.

    :param AppConfig: The base configuration class.
    :type AppConfig: django.apps.AppConfig

    :cvar default_auto_field: The default auto field for models.
    :vartype default_auto_field: str
    :cvar name: The name of the app.
    :vartype name: str
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'band'
