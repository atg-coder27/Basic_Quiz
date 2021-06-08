from django.apps import AppConfig



class BaseappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'BaseApp'

    def ready(self) -> None:
        from scheduler import updater
        updater.start()