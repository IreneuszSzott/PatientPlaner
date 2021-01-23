from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.utils.html import  escape


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_patient = models.BooleanField(default = False)
    is_doctor = models.BooleanField(default = False)

# Create your models here.
