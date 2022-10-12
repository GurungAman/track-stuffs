from movie.models import Movie
from movie.serializers import MovieSerializer

from common.viewset import ModelViewSet
from movie.filter import MovieFilter


class MovieViewSet(ModelViewSet):
    model_class = Movie
    serializer_class = MovieSerializer
    filterset_class = MovieFilter
