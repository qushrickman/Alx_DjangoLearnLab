from importlib.resources import path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, unlike_post, like_post

from django.urls import path
from .views import like_post

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = router.urls 
urlpatterns += [
    path("posts/<int:pk>/like/", like_post, name="like-post"),
    path("posts/<int:pk>/unlike/", unlike_post, name="unlike-post"),
]