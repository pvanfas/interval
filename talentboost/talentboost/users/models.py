from django.contrib.auth.models import AbstractUser
from django.db import models

USERTYPE_CHOICES = (
    ("Administrator", "Administrator"),
    ("DistrictConvenor", "District Convenor"),
    ("ZonalConvenor", "Zonal Convenor"),
    ("CenterConvenor", "Center Convenor"),
    ("Student", "Student"),
)


class CustomUser(AbstractUser):
    usertype = models.CharField(max_length=20, choices=USERTYPE_CHOICES, default="Student")

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username
