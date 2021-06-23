from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from notifications.api.serializers.notification_count_serializers import NotificationCountSerializer
from notifications.constant_variables import NotificationStatus
from notifications.models.notification_count import NotificationCount
from notifications.models.notification_history import NotificationHistory


class NotificationCountViewSet(mixins.RetrieveModelMixin,
                               mixins.DestroyModelMixin,
                               mixins.ListModelMixin,
                               GenericViewSet):
    queryset = NotificationCount.objects.all()
    serializer_class = NotificationCountSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        notifications = NotificationHistory.objects.filter(to_user=user, status=NotificationStatus.NEW)
        if len(notifications) != NotificationCount.objects.get(user=user).quantity:
            NotificationCount.objects.filter(user=user).update(quantity=len(notifications))
        return NotificationCount.objects.filter(user=user)
