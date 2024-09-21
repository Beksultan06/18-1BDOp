from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(
        max_length=155,
        verbose_name='Номер телефона'
    )

    def __str__(self) -> str:
        return self.username
    
    class Meta:
        verbose_name_plural = 'Пользователи'