# /backend/customer/urls.py.
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from customer import views

urlpatterns = [
    path('customer/', views.CustomerList.as_view()),
    path('customer/<int:pk>/', views.CustomerDetail.as_view()),
]