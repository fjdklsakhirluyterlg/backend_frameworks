from django.db import models


from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
# Create your models here.


class Myuser(User):
    def __init__(self):
        pass