from django.urls import path
from book.views import BookList

urlpatterns = [
    path('book/', BookList.as_view(), name='book_list')
]



