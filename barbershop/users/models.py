from datetime import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

def update_last_login(sender, user, **kwargs):
    """
    A signal receiver which updates the last_login date for
    the user logging in.
    """
    user.last_login = timezone.now()
    user.save(update_fields=["last_login"])
