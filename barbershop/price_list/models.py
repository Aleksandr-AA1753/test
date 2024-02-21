from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.urls import reverse



# Create your models here.


class Price(models.Model):
    title = models.CharField(max_length = 250, blank = False, verbose_name = "Заголовок")
    slug = models.SlugField(max_length = 250, unique = True, db_index = True, verbose_name = "Slug",
        validators = [
            MinLengthValidator(5, message = "Минимум 5 символов"),
            MaxLengthValidator(100, message = "Максимум 100 символов")
        ])
    content = models.TextField(blank = True, verbose_name = "Описание")
    category = models.ForeignKey('Category', on_delete=models.PROTECT, 
        related_name='posts', verbose_name = 'Категории')
    is_price = models.DecimalField(max_digits=6, decimal_places=2, blank = False, null=True,
        verbose_name = "Цена")
    published = models.BooleanField(default = True, verbose_name = "Опубликовать")
    not_published = models.BooleanField(default = False, verbose_name = "Снять с публикации")
    photo = models.ImageField(upload_to = "photos/%Y/%m/%d", default = None, blank = True, 
        null = True, verbose_name = "Загрузите фото")

    for_man = models.BooleanField(default=False, verbose_name = "Для мужчин")
    for_woman = models.BooleanField(default=False, verbose_name = "Для женщин")
   


    class Meta:
        verbose_name = 'Прайс'
        verbose_name_plural = "Прайс"


    def __str__(self):
        return str([
            self.title,
            self.slug,
            self.content,
            self.category,
            self.is_price,
            self.published,
            self.not_published,
            self.photo,
            self.for_man,
            self.for_woman,
        ])


class Category(models.Model):
    name = models.CharField(max_length = 100, db_index = True, verbose_name="Категория")
    slug = models.SlugField(max_length = 250, unique = True, db_index = True)

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = "Категории"


    def __str__(self):
        return self.name
    




a = Price.objects.all()
for i in a:
    print(i)
  
