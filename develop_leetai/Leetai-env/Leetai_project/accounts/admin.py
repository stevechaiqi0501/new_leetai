from django.contrib import admin
from .models import CustomUser
# Register your models here.
# adminは、管理パネルに関する操作を記述する

admin.register(CustomUser)

