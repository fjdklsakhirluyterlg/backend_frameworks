from django.db import models

from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _

from .managers import UserManager

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(_('user name'), max_length=30, blank=True)
    password = models.CharField(_('password'), max_length=128)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    objects = UserManager()

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)