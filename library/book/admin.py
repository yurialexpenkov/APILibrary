from django.contrib import admin
from book.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'isbn', 'year_of_release', 'number_of_pages']


admin.site.register(Book, BookAdmin)
