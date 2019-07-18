from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.backends import ModelBackend


class EmailModelBackend(ModelBackend):
    def authenticate(self, request,  username=None, password=None,  **kwargs):
        kwargs = {'email': username}
        print("Sadasd")
        print(username)
        print(password)
        try:
            user = User.objects.get(**kwargs)
            if user.has_usable_password() and user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
