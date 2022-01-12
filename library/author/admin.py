from django.contrib import admin
from author.models import Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'birthday']


admin.site.register(Author, AuthorAdmin)

