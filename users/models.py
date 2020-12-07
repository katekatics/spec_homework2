from django.contrib.auth.models import AbstractUser
from django.db import models


class RegularUser(AbstractUser):
    phone_number = models.TextField(
        'Номер телефона',
        null=False,
        blank=False
    )
    postal_code = models.TextField(
        'Почтовый индекс',
        null=False,
        blank=False
    )
    age = models.PositiveIntegerField(
        'Возраст',
        null=True,
        blank=True
    )
    sex = models.BooleanField(
        'Пол',
        null=True,
        blank=True
    )
