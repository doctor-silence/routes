from django.apps import AppConfig

# Настройка отображения меню админки
class TrainsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'trains'
    verbose_name = 'Поезда'
