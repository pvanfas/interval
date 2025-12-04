from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

USERTYPE_CHOICES = (
    ("Administrator", "Administrator"),
    ("Teacher", "Teacher"),
    ("Student", "Student"),
)


class CustomUser(AbstractUser):
    usertype = models.CharField(max_length=20, choices=USERTYPE_CHOICES, default="Student")
    photo = models.ImageField(upload_to="users/", default="users/avatar.png", blank=True, null=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def get_photo(self):
        return (settings.DOMAIN + self.photo.url) if self.photo else settings.DEFAULT_AVATAR

    def __str__(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        else:
            return self.username
