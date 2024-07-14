from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    Studenttype=models.BooleanField(default=False)
    picture=models.ImageField(verbose_name='プロフィールの画像',blank=True,null=True)
    class Meta:
        verbose_name_plural = "CustomUser"