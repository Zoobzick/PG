from django.contrib.auth.models import AbstractUser
from django.db import models

from authapp.managers import CustomUserManager


# Create your models here.


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True, null=False, blank=False,
                              verbose_name="Почта")
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
