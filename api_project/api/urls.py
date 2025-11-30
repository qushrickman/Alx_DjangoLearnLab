from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Simple ListAPIView (from previous task)
    path('books/', BookList.as_view(), name='book-list'),

    # CRUD ViewSet routes
    path('', include(router.urls)),
]
