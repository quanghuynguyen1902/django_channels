from rest_framework.permissions import BasePermission
from users.models import User


class CheckAppKey(BasePermission):
    def has_permission(self, request, view):
        # API_KEY should be in request headers to authenticate requests
        app_key = request.META.get('HTTP_APP_KEY')
        user = User.objects.filter(app_key=app_key).exists()
        return user