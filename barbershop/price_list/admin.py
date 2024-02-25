from django.contrib import admin
from . import models
from .models import Price


@admin.register(Price)
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}



#admin.site.register(models.Price)
admin.site.register(models.Category)
admin.site.register(models.Stock)
admin.site.register(models.Customers)



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