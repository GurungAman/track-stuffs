from datetime import datetime, timedelta
import uuid
import jwt
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .user_manager import UserManager

# Create your models here.


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_('email address'), blank=False, unique=True)
    is_admin = models.BooleanField(_("admin flag"), default=False)
    public_movie = models.BooleanField(_("public movie list"), default=False)
    public_tvshow = models.BooleanField(
        _("public Tv Show list"), default=False)
    public_game = models.BooleanField(_("public game list"), default=False)

    username = None

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def token(self):
        token = jwt.encode(
            {
                'id': str(self.id),
                'email': self.email,
                'is_admin': self.is_admin,
                'exp': datetime.utcnow() + timedelta(hours=settings.JWT_EXPIRY_TIME)
            },
            settings.SECRET_KEY,
            algorithm='HS256'
        )
        return token
