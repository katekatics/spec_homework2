from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(
        'Название книги',
        max_length=250
    )
    author = models.CharField(
        'Автор книги',
        max_length=200
    )
    rating = models.IntegerField(
        'Рейтинг книги'
    )
    date = models.DateTimeField(
        'Дата размещения на сервисе',
        auto_now_add=True
    )
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name='Пользователь, разместивший книгу'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_book', args=[str(self.id)])
