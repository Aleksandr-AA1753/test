from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView


from price_list import models



# Create your views here.

class BarbershopHome(ListView):
    template_name = 'price_list/index.html'
    context_object_name = 'category'
    title_page = 'Главная страница'
    
    def get_queryset(self):
        return models.Price.objects.all().select_related('title')
    