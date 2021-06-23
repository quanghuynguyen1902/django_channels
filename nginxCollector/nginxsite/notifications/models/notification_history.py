from django.contrib.postgres.fields import JSONField
from django.db import models
from notifications.constant_variables import NotificationStatus, NOTIFICATION_STATUS
from users.models import User


class NotificationHistory(models.Model):
    title = models.TextField(default='', blank=True)
    to_user = models.ForeignKey(User, null=True, blank=False, on_delete=models.CASCADE)
    content = models.TextField(default='', blank=True)
    status = models.CharField(
        max_length=1,
        choices=NOTIFICATION_STATUS,
        default=NotificationStatus.NEW
    )
    created_at = models.DateTimeField(auto_now_add=True)
    last_read = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    class Meta:
        verbose_name_plural = "notification_histories"

    def __str__(self):
        return self.template.__str__() + ' *** to *** ' + self.to_user.__str__()
