from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    telephone_number = models.BigIntegerField(db_index = True,
            unique = True, verbose_name = "Номер телефона")
    photo = models.ImageField(upload_to = "users/%Y/%m/%d/", blank = True, 
            null = True, verbose_name = "Фотография")
    birthday = models.DateTimeField(blank = True, null = True, 
            verbose_name = "Дата рождения")
