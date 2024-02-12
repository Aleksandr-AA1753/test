from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.contrib.auth import get_user_model

# Create your views here.




class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()

    extra_context = {
        'title': "Профиль пользователя"
    }
