from django.contrib.auth import get_user_model
from django.core.signing import TimestampSigner


signer = TimestampSigner()


class TokenBackend(object):

    def authenticate(self, token=None):
        if token:
            username = signer.unsign(token, max_age=600)
            return get_user_model().objects.get(username=username)
        return None

    def get_user(self, user_id):
        try:
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None
