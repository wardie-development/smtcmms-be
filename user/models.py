from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from customer.models import Customer


def profile_image_directory_path(instance, filename):
    date_now = datetime.now()
    date = date_now.strftime("%d%m%Y_%H:%M:%S")

    return f"media/{instance.first_name}_{date}_{filename}"


class UserModel(AbstractUser):
    customer = models.ForeignKey(
        Customer, related_name="users", on_delete=models.CASCADE, null=True, blank=True
    )

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
