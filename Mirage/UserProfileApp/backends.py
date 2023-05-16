from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class UsernameEmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()

        if '@' in username: # type: ignore
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}

        try:
            user = UserModel.objects.get(**kwargs)
            if user.check_password(password): # type: ignore
                return user
        except UserModel.DoesNotExist:
            return None

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
