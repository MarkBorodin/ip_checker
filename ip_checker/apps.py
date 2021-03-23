from django.apps import AppConfig


class IpCheckerConfig(AppConfig):
    name = 'ip_checker'

    def ready(self):
        import ip_checker.signals  # noqa
