from django.db import models
from django.contrib.auth import get_user_model
from django.db import models
from .helper import BaseModel

User = get_user_model()

# Create your models here.
STATUS_CHOICES = (
    # status for movies and tv shows
    ('C', 'Completed'),
    ('D', 'Dropped'),
    ('P', 'Plan to watch'),
    ('W', 'Watching')
)


class Movie(BaseModel):
    user = models.ForeignKey(User, related_name='movie',
                             on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='P'
    )

    class Meta:
        unique_together = ('user', 'name')


class TvShow(BaseModel):
    user = models.ForeignKey(User, related_name='show',
                             on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='P'
    )
    season = models.PositiveIntegerField(default=1)
    episode = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('user', 'name')


class Game(BaseModel):
    user = models.ForeignKey(User, related_name='game',
                             on_delete=models.CASCADE)
    GAME_STATUS_CHOICES = (
        ('C', 'Completed'),
        ('D', 'Dropped'),
        ('P', 'Plan to play'),
        ('W', 'currently playing'),
    )
    status = models.CharField(
        max_length=20,
        choices=GAME_STATUS_CHOICES,
        default='P'
    )

    class Meta:
        unique_together = ('user', 'name')
