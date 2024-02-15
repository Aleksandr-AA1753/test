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
    published = models.BooleanField(default = False, verbose_name = "Опубликовать")
    category = models.ForeignKey('Category', on_delete=models.PROTECT, 
        related_name='posts', verbose_name = 'Категории')
    is_price = models.DecimalField(max_digits=6, decimal_places=2, blank = False, null=True,
        verbose_name = "Цена")
    for_man = models.BooleanField(default=False, verbose_name = "Для мужчин")
    for_woman = models.BooleanField(default=False, verbose_name = "Для женщин")


    class Meta:
        verbose_name = 'Прайс'
        verbose_name_plural = "Прайс"


    def __str__(self):
        return self.title



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
    print (i.title, i.content)   