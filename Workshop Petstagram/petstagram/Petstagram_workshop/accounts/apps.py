from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Petstagram_workshop.accounts'

    def ready(self):
        import Petstagram_workshop.accounts.signals

# Every time you use signals you have to import them into the app module.
