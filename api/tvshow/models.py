from enum import Enum
from django.db import models
from django.contrib.auth import get_user_model
from django.db import models
from common.models import BaseModel

User = get_user_model()


class TvshowStatusChoice(Enum):
    completed = ('C', 'Completed watching the show')
    dropped = ('D', 'Stopped watching mid-way')
    plan_to_watch = ('P', 'Plan to watch in the future')
    watching = ('W', 'Watching now')


class TvShow(BaseModel):
    user = models.ForeignKey(User, related_name='show',
                             on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=[x.value for x in TvshowStatusChoice],
        default=TvshowStatusChoice.plan_to_watch.value[0]
    )

    season = models.PositiveIntegerField(default=1)
    episode = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('user', 'name')
