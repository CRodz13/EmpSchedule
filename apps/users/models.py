from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    name = models.CharField(_("Name of User"), max_length=255, blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)

    def get_absolute_url(self):
        # Get url for user's detail view.  Returns: str: URL for user detail
        return reverse("users:detail", kwargs={"username": self.username})
