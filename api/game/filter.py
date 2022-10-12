from game.models import Game
from common.filter import BaseFilter


class GameFilter(BaseFilter):
    class Meta:
        model = Game
        fields = ['name', 'status']
