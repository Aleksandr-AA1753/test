from django.contrib import admin
from django.urls import include, path
from . import views


admin.site.site_header = "Страница управления"
admin.site.index_title = "Категории управления"

urlpatterns = [
    path('', views.BarbershopHome.as_view(), name='home'),
]