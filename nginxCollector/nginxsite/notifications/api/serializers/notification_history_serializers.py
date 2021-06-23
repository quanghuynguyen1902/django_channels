from rest_framework import serializers
from notifications.models.notification_history import NotificationHistory


class NotificationHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationHistory
        fields = '__all__'
        read_only_fields = ['to_user', 'content', 'created_at']
