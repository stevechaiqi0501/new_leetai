from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    Studenttype=models.BooleanField(default=False)
    picture=models.ImageField(verbose_name='プロフィールの画像',blank=True,null=True)
    discription=models.CharField(max_length=100,default='')
    sex=models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = "CustomUser"