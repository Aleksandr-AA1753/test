from django.contrib import admin
#from . import models
from .models import Price, Category, Stock, Customers


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"category_slug": ["category_name"]}


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["stock_title"]}


@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    prepopulated_fields = {"customers_slug": ["customers_name"]}

"""
admin.site.register(models.Price)
admin.site.register(models.Category)
admin.site.register(models.Stock)
admin.site.register(models.Customers)
"""


"""
@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'content', 'photo', 'category', ]
    readonly_fields = ['post_photo']
    prepopulated_fields = {"slug": ("title", )}
    filter_vertical = ['tags']
    list_display = ('title', 'post_photo', 'time_create', 'is_published', 'cat')
    list_display_links = ('title', )
    ordering = ['-time_create', 'title']
    list_editable = ('is_published', )
    actions = ['set_published', 'set_draft']
    search_fields = ['title__startswith', 'cat__name']
    list_filter = ['is_published']
    save_on_top = True

"""