from django import views
from django.urls import path
from users import views

app_name = "users"


urlpatterns = [
    path('profile/', views.ProfileUser.as_view(), name='profile'),
]