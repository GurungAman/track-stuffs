from django.contrib.auth import get_user_model
from tvshow.models import TvShow
from tvshow.serializers import TvShowSerializer
from tvshow.filter import TvShowFilter
from common.viewset import ModelViewSet

User = get_user_model()


class TvShowViewSet(ModelViewSet):
    model_class = TvShow
    serializer_class = TvShowSerializer
    filterset_class = TvShowFilter
