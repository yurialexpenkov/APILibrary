from django.urls import path
from author.views import AuthorList, AuthorDetail

urlpatterns = [
    path('author/', AuthorList.as_view(), name='author_list'),
    path('author/<int:pk>/', AuthorDetail.as_view(), name='author_detail')
]



