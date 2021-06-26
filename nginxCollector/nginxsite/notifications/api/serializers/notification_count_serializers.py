from rest_framework import serializers
from notifications.models.notification_count import NotificationCount


class NotificationCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationCount
        fields = '__all__'
        read_only_fields = ['user', 'quantity']
