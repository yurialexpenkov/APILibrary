from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from book.serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework
from book.models import Book
from author.models import Author


class PaginationBook(PageNumberPagination):
    """Пагинация списка книг"""
    page_size = 2
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'result': data

        })


class BookFilter(rest_framework.FilterSet):
    """Фильтрация списка книг"""
    number_of_pages = rest_framework.RangeFilter()


class BookList(ListModelMixin, GenericAPIView):
    """Представление для получения списка книг"""
    serializer_class = BookSerializer
    pagination_class = PaginationBook
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BookFilter

    def get_queryset(self):
        queryset = Book.objects.all()
        book_title = self.request.query_params.get('title')
        book_author = self.request.query_params.get('author')
        if book_title:
            queryset = queryset.filter(title=book_title)
        if book_author:
            queryset = queryset.filter(author__name=book_author)
        return queryset

    def get(self, request):
        return self.list(request)
