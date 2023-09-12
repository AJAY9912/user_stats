from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError

from .managers import CustomUserManager



class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name



class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True, validators=[EmailValidator])
    status = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    roles = models.ManyToManyField(Role, null=True, blank=True, related_name="user")
    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def clean(self):
        if not self.status:
            raise ValidationError("user is not active")






