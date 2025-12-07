from rest_framework import generics, permissions, mixins
from .models import Book
from .serializers import BookSerializer


# -------------------------------
# LIST VIEW
# -------------------------------
class BookListView(mixins.ListModelMixin,
                   generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# -------------------------------
# DETAIL VIEW
# -------------------------------
class BookDetailView(mixins.RetrieveModelMixin,
                     generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


# -------------------------------
# CREATE VIEW
# -------------------------------
class BookCreateView(mixins.CreateModelMixin,
                     generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save()


# -------------------------------
# UPDATE VIEW
# -------------------------------
class BookUpdateView(mixins.UpdateModelMixin,
                     generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save()


# -------------------------------
# DELETE VIEW
# -------------------------------
class BookDeleteView(mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
