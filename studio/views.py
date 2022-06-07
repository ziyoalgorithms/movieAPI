
from studio.serializers import ActorSerializer, MovieSerializer, CommentSerializer
from .models import  Actor, Movie, Comment
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend



class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    ordering_fields = ["imdb", "-imdb"]
    filterset_fields = ["genre"]
    search_fields = ["name", "year", "imdb", "genre"]

    @action(detail=True, methods=['POST'])
    def add_actor(self, request, *args, **kwargs):
        movie = self.get_object()
        movie.actors.add(request.data)
        serializer = MovieSerializer(movie)
        return Response(data=serializer.data)

    @action(detail=True, methods=['POST'])
    def remove_actor(self, request, *args, **kwargs):
        movie = self.get_object()
        movie.actors.remove(request.data)
        serializer = MovieSerializer(movie)
        return Response(data=serializer.data)


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer



class MovieActorAPIView(APIView):
    def get(self, reuqest, id):
        movie = Movie.objects.get(id=id)
        serializer = ActorSerializer(movie.actors.all(), many=True)

        return Response(data=serializer.data)



class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Comment.objects.all()

    def perform_create(self, serializer):
        serializer.validated_data['user_id'] = self.request.user
        serializer.save()



class AddCommentAPIView(APIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )

    def post(self, request):
        new_comment = request.data
        serializer = CommentSerializer(data=new_comment)
        if serializer.is_valid():
            serializer.validated_data['user_id'] = self.request.user
            serializer.save()
            return Response(data=serializer.data)
        else:
            raise ValidationError(detail="Xato!")


class ListCommentAPIView(APIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )

    def get(self, requst):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)

        return Response(data=serializer.data)


class DeleteCommentAPIView(APIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )

    def post(self, request):
        comment = get_object_or_404(Comment, id=request.data["id"])
        comment.delete()
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(data=serializer.data)
