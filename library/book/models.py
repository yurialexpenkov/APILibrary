from django.db import models

from author.models import Author


class Book(models.Model):
    """Модель книги"""
    title = models.CharField(max_length=100, verbose_name='Название')
    isbn = models.CharField(max_length=100, verbose_name="Международный стандартный книжный номер")
    year_of_release = models.DateTimeField(verbose_name="дата выпуска")
    number_of_pages = models.IntegerField(verbose_name="Количество страниц")
    author = models.ManyToManyField(Author, related_name='author', blank=True, null=True, verbose_name='автор')


    def __str__(self):
        return self.title