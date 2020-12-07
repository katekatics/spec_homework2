from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Journal(models.Model):
    title = models.CharField(
        'Название журнала',
        max_length=250
    )
    editor = models.CharField(
        'Редактор журнала',
        max_length=100
    )
    page_count = models.IntegerField(
        'Количество страниц журнала'
    )
    date = models.DateTimeField(
        'Дата размещения на сервисе',
        auto_now_add=True
    )
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name='Пользователь, разместивший журнал'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_journal', args=[str(self.id)])
