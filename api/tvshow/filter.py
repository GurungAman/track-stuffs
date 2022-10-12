from tvshow.models import TvShow
from common.filter import BaseFilter


class TvShowFilter(BaseFilter):
    class Meta:
        model = TvShow
        fields = ['name', 'status']
