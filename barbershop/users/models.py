from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length = 50, db_index=True, 
            verbose_name = "Имя")
    last_name = models.CharField(max_length = 50, db_index= True,
            verbose_name = "Фамилия")
    email = models.EmailField(max_length = 50, db_index = True, 
            unique = True, verbose_name = "Электронная почта")
    telephone_number = models.BigIntegerField(db_index = True, 
            unique = True, verbose_name = "Номер телефона")


class User(AbstractUser):
    photo = models.ImageField(upload_to = "users/%Y/%m/%d/", blank = True, 
            null = True, verbose_name = "Фотография")
    birthday = models.DateTimeField(blank = True, null = True, 
            verbose_name = "Дата рождения")
