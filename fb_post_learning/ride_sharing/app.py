from django.apps import AppConfig


class RideSharingAppConfig(AppConfig):
    name = "ride_sharing"

    def ready(self):
        from ride_sharing import signals # pylint: disable=unused-variable
