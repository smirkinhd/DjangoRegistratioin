# registration_app/apps.py
from django.apps import AppConfig

class RegistrationAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'registration_app'
    verbose_name = 'Регистрация пользователей'