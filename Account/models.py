from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    image = models.ImageField(_("image"), upload_to = 'users_avatars', null=True, blank=True)
