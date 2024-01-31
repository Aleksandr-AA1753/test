from django import views
from django.urls import path
from users import views


urlpatterns = [
    path('', views.index, name='index'),
]