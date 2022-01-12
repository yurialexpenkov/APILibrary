from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from author.models import Author
from author.serializers import AuthorSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PaginationAuthor(PageNumberPagination):
    """Пагинация списка авторов"""
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


class AuthorList(ListModelMixin, CreateModelMixin, GenericAPIView):
    """Представление для получения списка авторов"""
    serializer_class = AuthorSerializer
    pagination_class = PaginationAuthor

    def get_queryset(self):
        queryset = Author.objects.all()
        author_name = self.request.query_params.get('name')
        if author_name:
            queryset = self.queryset.filter(name=author_name)
        return queryset

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return  self.create(request)



class AuthorDetail(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericAPIView):
    """Представление для получения детальной информации о товаре, а также для его редактирования и удаления"""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self. destroy(request, *args, **kwargs)

    # def get_queryset(self):
    #     queryset = Author.objects.all()
    #     author_name = self.request.query_params.get('name')
    #     if author_name:
    #         queryset = queryset.filter(name=author_name)
    #     return queryset



# class ItemList(ListModelMixin, CreateModelMixin, GenericAPIView):
#     serializer_class = ItemSerializer
#
#     def get_queryset(self):
#         queryset = Item.objects.all()
#         item_name = self.request.query_params.get('name')
#         if item_name:
#             queryset = queryset.filter(name=item_name)
#         return queryset
#
#
#     def get(self, request):
#         return self.list(request)


# class ItemList(ListModelMixin, CreateModelMixin, GenericAPIView):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer
#
#     def get(self, request):
#         return self.list(request)