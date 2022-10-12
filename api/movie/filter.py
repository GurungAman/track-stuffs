from movie.models import Movie
from common.filter import BaseFilter


class MovieFilter(BaseFilter):
    class Meta:
        model = Movie
        fields = ['name', 'status']
