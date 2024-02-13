from django.contrib import admin
from django.urls import include, path
from barbershop.price_list import views

urlpatterns = [
    path('/', views.index, name = 'home'),
]