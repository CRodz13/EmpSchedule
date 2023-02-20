from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    name = CharField(_("Name of User"), max_length=255, blank=True)
    first_name = None
    last_name = None

    def get_absolute_url(self):
        # Get url for user's detail view.  Returns: str: URL for user detail
        return reverse("users:detail", kwargs={"username": self.username})
