from rest_framework import serializers
from book.models import Book

class AuthorBookField(serializers.RelatedField):
    def to_representation(self, value):
        return value.name



class BookSerializer(serializers.ModelSerializer):
    author = AuthorBookField(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ('title', 'isbn', 'year_of_release', 'number_of_pages', 'author')
