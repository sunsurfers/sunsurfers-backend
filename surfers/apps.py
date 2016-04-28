from django.apps import AppConfig

from django.conf import settings
from django.db.models import signals

from tastypie.models import create_api_key

from surfers.signals import create_latest_point


class SurfersConfig(AppConfig):
    name = 'surfers'

    def ready(self):
        print("Ready called!")
        signals.post_save.connect(create_latest_point,
                                  sender=settings.AUTH_USER_MODEL,
                                  dispatch_uid="create_latest_point")
        signals.post_save.connect(create_api_key,
                                  sender=settings.AUTH_USER_MODEL,
                                  dispatch_uid="create_user_api_key")
