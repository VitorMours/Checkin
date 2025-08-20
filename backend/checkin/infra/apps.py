from django.apps import AppConfig


class CheckinConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkin.infra'


    def ready(self):
        import checkin.infra.db.models