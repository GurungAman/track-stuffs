from django.contrib.auth import get_user_model
from game.models import Game
from game.serializers import GameSerializer
from game.filter import GameFilter
from common.viewset import ModelViewSet

User = get_user_model()


class GameViewSet(ModelViewSet):
    model_class = Game
    serializer_class = GameSerializer
    filterset_class = GameFilter
