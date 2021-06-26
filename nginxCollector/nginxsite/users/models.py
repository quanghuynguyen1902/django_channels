from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import MinValueValidator
from django.db import models
import uuid
class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('User must have an email')
        if not username:
            raise ValueError('User must have username')

        user = self.model(
            email=self.normalize_email(email),
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_moderator = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    app_id = models.CharField(max_length=224, editable=False, unique=True)
    username = models.CharField(max_length=224, null=False, blank=False)
    email = models.EmailField(verbose_name='email', max_length=224, null=False, blank=False, unique=True)
    app_key = models.CharField(max_length=224, null=False, blank=False)
    api_identify = models.CharField(max_length=524, null=False, blank=False)
    authorization_field = models.CharField(max_length=224, null=False, blank=False)
    created_at = models.DateTimeField(verbose_name='created at', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='updated at', auto_now=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    slug = models.SlugField(default='', max_length=255, unique=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_moderator = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        """String for representing the Model object."""
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

