from django.apps import AppConfig


class FbPostAuthAppConfig(AppConfig):
    name = "fb_post_auth"

    def ready(self):
        from fb_post_auth import signals # pylint: disable=unused-variable
