from django.contrib.auth import get_user_model

from rest_framework.viewsets import GenericViewSet
from rest_framework.exceptions import ValidationError, PermissionDenied
from rest_framework import status
from rest_framework.response import Response

from viewset_mixin import ModelViewSet
from exception.exceptions import InvalidCategoryError

from .models import Movie, TvShow, Game
from .serializers import MovieSerializer, TvShowSerializer, GameSerializer
from authentication.jwt import AnnonymousUserAuth


User = get_user_model()


class MovieViewSet(ModelViewSet):
    model_class = Movie
    serializer_class = MovieSerializer


class TvShowViewSet(ModelViewSet):
    model_class = TvShow
    serializer_class = TvShowSerializer


class GameViewSet(ModelViewSet):
    model_class = Game
    serializer_class = GameSerializer


class ShareListView(GenericViewSet):
    authentication_classes = (AnnonymousUserAuth,)

    def get_serializer_class(self, *args, **kwargs):
        category = kwargs.get('category')
        serializer_classes = {
            'movie': MovieSerializer,
            'tv-show': TvShowSerializer,
            'game': GameSerializer,
        }
        return serializer_classes.get(category)

    def check_user_permission(self, request, user, category):
        if category == 'movie' and not user.public_movie:
            raise PermissionDenied
        if category == 'tv-show' and not user.public_tvshow:
            raise PermissionDenied
        if category == 'game' and not user.public_game:
            raise PermissionDenied

    def get_queryset(self, category, *args, **kwargs):
        models = {
            'movie': Movie,
            'tv-show': TvShow,
            'game': Game,
        }
        return models.get(category).objects.filter(*args, **kwargs)

    def list(self, request, user_id, category):
        user = User.objects.filter(id=user_id).first()
        if not user:
            raise ValidationError('Invalid user')
        serializer_class = self.get_serializer_class(category=category)
        if not serializer_class:
            raise InvalidCategoryError

        if request.user.id != user_id:
            self.check_user_permission(request, user, category)
        queryset = self.get_queryset(category)
        serializer = serializer_class(queryset, many=True)

        response = {
            "success": True,
            "data": serializer.data
        }
        return Response(response, status.HTTP_200_OK)
