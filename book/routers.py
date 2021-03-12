#./routers.py
from rest_framework import routers
from book.viewsets import BookViewSet
router = routers.SimpleRouter()
router.register(r'book', BookViewSet, basename='book')


#backend/urls.py
from django.contrib import admin
from django.urls import path, include
from routers import router

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('api/', include((router.urls, 'backend'), namespace='backend'))
]