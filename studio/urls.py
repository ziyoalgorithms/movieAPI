
from django.urls import path, include
from .views import ActorViewSet, MovieViewSet, MovieActorAPIView, CommentViewSet, AddCommentAPIView, ListCommentAPIView, DeleteCommentAPIView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken


router = DefaultRouter()
router.register('movies', MovieViewSet)
router.register('actors', ActorViewSet)
router.register('comments', CommentViewSet, 'comments')


urlpatterns = [
    path('', include(router.urls)),
    path('movies/<int:id>/actors/', MovieActorAPIView.as_view(), name='movie_actors'),
    path('auth/', ObtainAuthToken.as_view()),
    path('add_comment/', AddCommentAPIView.as_view()),
    path('list_comment/', ListCommentAPIView.as_view()),
    path('delete_comment/', DeleteCommentAPIView.as_view())
]