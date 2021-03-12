# /backend/book/urls.py.
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from book import views

urlpatterns = [
    path('book/', views.BookList.as_view()),
    path('book/<int:pk>/', views.BookDetail.as_view()),
]