from enum import Enum
from django.db import models
from django.contrib.auth import get_user_model
from django.db import models
from common.models import BaseModel

User = get_user_model()


class MovieStatusChoice(Enum):
    completed = ('C', 'Completed watching movie')
    dropped = ('D', 'stopped watching mid-way')
    plan_to_watch = ('P', 'Plan to watch in the future')
    watching = ('W', 'Watching now')


class Movie(BaseModel):
    user = models.ForeignKey(User, related_name='movie',
                             on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=[x.value for x in MovieStatusChoice],
        default=MovieStatusChoice.plan_to_watch.value[0]
    )

    class Meta:
        unique_together = ('user', 'name')
