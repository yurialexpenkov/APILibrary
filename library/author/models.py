from django.db import models


class Author(models.Model):
    """Модель автора"""
    name = models.CharField(max_length=100, verbose_name='Имя')
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    birthday = models.DateTimeField(verbose_name='Дата рождения')

    def __str__(self):
        return self.name
