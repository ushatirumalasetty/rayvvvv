from django.apps import AppConfig


class FbPostCleanArchV2AppConfig(AppConfig):
    name = "fb_post_clean_arch_v2"

    def ready(self):
        from fb_post_clean_arch_v2 import signals # pylint: disable=unused-variable
