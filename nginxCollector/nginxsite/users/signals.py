from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.text import slugify
import uuid
from core.utils import generate_random_string, generate_app_key
from users.models import User
from notifications.models.notification_count import NotificationCount


@receiver(pre_save, sender=User)
def add_slug_to_user(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.email.split('@')[0])
        # Check if slug existed
        random_string = ''
        while True:
            if User.objects.filter(slug=slug+random_string).exists():
                random_string = generate_random_string(length=2)
            else:
                break
        instance.slug = slug + random_string

@receiver(pre_save, sender=User)
def add_app_key_to_user(sender, instance, *args, **kwargs):
    if instance and not instance.app_key:
        app_key = generate_app_key().decode('utf-8')
        while True:
            if User.objects.filter(app_key=app_key).exists():
                app_key = generate_app_key().decode('utf-8')
            else:
                break
        instance.app_key = app_key

@receiver(pre_save, sender=User)
def add_app_id_to_user(sender, instance, *args, **kwargs):
    if instance and not instance.app_id:
        app_id = uuid.uuid4().hex[:8]
        while True:
            if User.objects.filter(app_id=app_id).exists():
                app_id = uuid.uuid4().hex[:8]
            else:
                break
        instance.app_id = app_id

@receiver(post_save, sender=User)
def add_notification_count_to_user(sender, instance, *args, **kwargs):
    if not NotificationCount.objects.filter(user=instance):
        NotificationCount.objects.create(user=instance, quantity=0)
