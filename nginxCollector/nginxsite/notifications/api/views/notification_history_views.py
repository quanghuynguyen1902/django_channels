import json
from rest_framework import mixins, status
from rest_framework.decorators import action, permission_classes, api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from notifications.api.serializers.notification_history_serializers import NotificationHistorySerializer
from notifications.constant_variables import NotificationStatus
from notifications.models.notification_history import NotificationHistory
from users.permissions import CheckAppKey
from users.models import User

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class NotificationHistoryViewSet(mixins.RetrieveModelMixin,
                                 mixins.DestroyModelMixin,
                                 mixins.ListModelMixin,
                                 GenericViewSet):
    queryset = NotificationHistory.objects.all()
    lookup_field = 'slug'
    serializer_class = NotificationHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        NotificationHistory.objects.filter(to_user=user, status=NotificationStatus.NEW).update(
            status=NotificationStatus.UNREAD)
        return NotificationHistory.objects.filter(to_user=user).order_by("-created_at")

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        NotificationHistory.objects.filter(pk=instance.id).update(status=NotificationStatus.READ)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    


@api_view(['POST'])
@permission_classes([CheckAppKey])
def send_notification(request):
    app_key = request.META.get('HTTP_APP_KEY')
    user = User.objects.get(app_key=app_key)
    content = request.data['content']
    NotificationHistory.objects.create(to_user=user, content=content)
    room_group_name = 'notification_' + app_key
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
    
            room_group_name, 
            {
                "type": "notification_message",
                "message": content
            }

    )
    return Response(request.data, status=status.HTTP_200_OK)