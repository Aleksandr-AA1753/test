from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
# Create your models here.

class Price(models.Model):
    title = models.CharField(max_length = 250, verbose_name = "Заголовок")
    slug = models.SlugField(max_length = 250, unique = True, db_index = True, verbose_name = "Slug",
        validators = [
            MinLengthValidator(5, message = "Минимум 5 символов"),
            MaxLengthValidator(100, message = "Максимум 100 символов")
        ])
    content = models.TextField(blank = True, verbose_name = "Описание")
    is_published = models.BooleanField(default = True, verbose_name = "Статус")
    category = models.ForeignKey('Category', on_delete=models.PROTECT, 
        related_name='posts', verbose_name = 'Категории')
    
    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length = 100, db_index = True, verbose_name="Категория")
    slug = models.SlugField(max_length = 250, unique = True, db_index = True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name