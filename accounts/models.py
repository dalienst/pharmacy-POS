from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Extending django user model to add roles
    Registration of users
    """

    email = models.EmailField(
        _("email address"),
    )
    is_vendor = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("user-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return self.username


class Vendor(models.Model):
    """
    Vendor model
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(
        max_length=300,
    )
    contact = models.PositiveIntegerField(null=True, blank=True, default=0)
    location = models.CharField(
        max_length=300,
    )

    def get_absolute_url(self):
        return reverse("vendor-profile", args=[str(self.id)])

    def __str__(self) -> str:
        return self.user.username


class Customer(models.Model):
    """
    Store customers details.
    Ease for shipping and deliveries
    More fields to be added
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(
        max_length=300,
    )
    location = models.CharField(
        max_length=300,
    )
    contact = models.PositiveIntegerField(null=True, blank=True, default=0)

    def get_absolute_url(self):
        return reverse("customer-profile", args=[str(self.id)])

    def __str__(self) -> str:
        return self.user.username
