from enum import Enum
from django.db import models
from django.contrib.auth import get_user_model
from django.db import models
from common.models import BaseModel

User = get_user_model()


class GameStatusChoice(Enum):
    completd = ('C', 'Completed playthrough')
    dropped = ('D', 'Dropped/stopped playing after a while')
    plan_to_play = ('P', 'Plan to play in the future')
    playing = ('W', 'currently playing')


class Game(BaseModel):
    user = models.ForeignKey(User, related_name='game',
                             on_delete=models.CASCADE)

    status = models.CharField(
        max_length=20,
        choices=[x.value for x in GameStatusChoice],
        default=GameStatusChoice.plan_to_play.value[0]
    )

    class Meta:
        unique_together = ('user', 'name')
