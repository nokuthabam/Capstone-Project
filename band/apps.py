from django.apps import AppConfig


class BandConfig(AppConfig):
    """
    This class will configure the band app.
    Parameters:
        AppConfig: config
    Attributes:
        name: str
            """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'band'
