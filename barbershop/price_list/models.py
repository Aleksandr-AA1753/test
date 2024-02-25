from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.urls import reverse


# Create your models here.


# Категории видов предоставляемых услуг
class Category(models.Model):
    category_name = models.CharField(max_length = 100, verbose_name="Категория")
    category_slug = models.SlugField(max_length = 250, db_index = True, unique = True, verbose_name="Слаг")
    category_content = models.TextField(blank = True, verbose_name = "Описание категории")

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.category_name
    

# Виды клиентов
class Customers(models.Model):
    customers_name = models.CharField(max_length = 100, verbose_name="Категория клиента")
    customers_slug = models.SlugField(max_length = 250, db_index = True, unique = True, verbose_name ="Слаг")
    customers_content = models.TextField(blank = True, verbose_name = "Описание")

    class Meta:
        verbose_name = 'Категория клиента'
        verbose_name_plural = "Категории клиентов"

    def __str__(self):
        return self.customers_name


# Прайс
class Price(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, 
        related_name='category', verbose_name = 'Категории')
    is_customers = models.ForeignKey(Customers, null=True, default=None, 
        on_delete=models.CASCADE, related_name='customers', verbose_name = "Категория клиента")
    title = models.CharField(max_length = 250, blank = True, verbose_name = "Заголовок")
    slug = models.SlugField(max_length = 250, unique = True, db_index = True, verbose_name = "Slug",)
    content = models.TextField(blank = True, verbose_name = "Описание")
    is_price = models.IntegerField(blank = True, null=True, verbose_name = "Цена")
    published = models.BooleanField(default = True, verbose_name = "Опубликовать")
    not_published = models.BooleanField(default = False, verbose_name = "Снять с публикации")
    photo = models.ImageField(upload_to = "photos/%Y/%m/%d", default = None, blank = True, 
        null = True, verbose_name = "Загрузите фото")


    class Meta:
        verbose_name = 'Прайс'
        verbose_name_plural = "Прайс"

    def __str__(self):
        return self.title



# Акции
class Stock(models.Model):
    stock_title = models.CharField(max_length = 200, verbose_name = "Название акции")
    slug = models.SlugField(max_length = 250, unique = True, db_index = True, verbose_name = "Slug",
        validators = [
            MinLengthValidator(5, message = "Минимум 5 символов"),
            MaxLengthValidator(250, message = "Максимум 250 символов")
        ])
    stock_content = models.TextField(blank = True, verbose_name = "Описание акции")
    old_price = models.IntegerField(blank = True, null=True, verbose_name = "Старая цена")
    new_price = models.IntegerField(blank = True, null=True, verbose_name = "Цена по акции")
    published = models.BooleanField(default = True, verbose_name = "Опубликовать")
    not_published = models.BooleanField(default = False, verbose_name = "Снять с публикации")
    photo = models.ImageField(upload_to = "photos/%Y/%m/%d", default = None, blank = True, 
        null = True, verbose_name = "Загрузите фото")
    start_date = models.DateField(auto_now_add = False, null = True, blank = True, 
        verbose_name = "Дата начала акции")
    stop_date = models.DateField(auto_now_add = False, null = True, blank = True, 
        verbose_name = "Дата окончания акции")
    for_man = models.BooleanField(default=False, verbose_name = "Для мужчин")
    for_woman = models.BooleanField(default=False, verbose_name = "Для женщин")


    class Meta:
        verbose_name = "Акция"
        verbose_name_plural = "Акции"

    def __str__(self):
        return self.stock_title
    



    
"""
for i in Price.objects.all():
    print('Заголовок: ', i.title, 'содержание: ', i.content, 'Слаг: ', i.slug)


for i in Stock.objects.all():
    print('Заголовок: ', i.stock_title,", ", "Слаг: ", i.slug, ", ", "Описание: ", i.stock_content,)
"""