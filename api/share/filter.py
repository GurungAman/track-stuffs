from django_filters.rest_framework import DjangoFilterBackend

from movie.filter import MovieFilter
from tvshow.filter import TvShowFilter
from game.filter import GameFilter


class ShareFilterBackend(DjangoFilterBackend):
    def get_filterset_class(self, view, queryset=None):
        category = view.kwargs.get('category')
        category_mapping = {
            'movie': MovieFilter,
            'tv-show': TvShowFilter,
            'game': GameFilter,
        }
        return category_mapping.get(category)
