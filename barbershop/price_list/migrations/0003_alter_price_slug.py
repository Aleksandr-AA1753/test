# Generated by Django 4.2.9 on 2024-02-15 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price_list', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='slug',
            field=models.SlugField(max_length=250, unique=True, verbose_name='Slug'),
        ),
    ]
