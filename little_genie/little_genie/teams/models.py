from django.db import models
from django.urls import reverse_lazy
from versatileimagefield.fields import VersatileImageField


class Team(models.Model):
    photo = VersatileImageField("Image", upload_to="images/team")
    name = models.CharField(max_length=250)
    designation = models.CharField(max_length=250)
    description = models.TextField()
    facebook_url = models.URLField(max_length=250, blank=True, null=True)
    twitter_url = models.URLField(max_length=250, blank=True, null=True)
    linkedin_url = models.URLField(max_length=250, blank=True, null=True)
    instagram_url = models.URLField(max_length=250, blank=True, null=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse_lazy("teams:view_team", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse_lazy("teams:update_team", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("teams:delete_team", kwargs={"pk": self.pk})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]
