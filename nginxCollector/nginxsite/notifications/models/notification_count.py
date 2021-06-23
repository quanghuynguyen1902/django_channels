from django.db import models
from django.contrib.postgres.fields import JSONField

from users.models import User


class NotificationCount(models.Model):
    user = models.ForeignKey(User, null=True, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "notification_counts"

    def __str__(self):
        return self.user.__str__() + ' *** ' + self.quantity.__str__()
