from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from apps.users.forms import UserAdminChangeForm, UserAdminCreationForm


User = get_user_model()
from .models import Schedule


admin.site.register(Schedule)