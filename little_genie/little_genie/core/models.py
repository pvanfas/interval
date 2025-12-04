import uuid

from django.db import models
from django.urls import reverse_lazy
from tinymce.models import HTMLField
from versatileimagefield.fields import VersatileImageField


class Testimonial(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    photo = VersatileImageField("Image", upload_to="images/Testimonials")
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse_lazy("core:view_testimonial", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse_lazy("core:update_testimonial", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("core:delete_testimonial", kwargs={"pk": self.pk})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]


class About(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    title = models.CharField(max_length=250)
    description = HTMLField()
    phone_number = models.CharField(max_length=20)
    phone_number2 = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField()
    little_genie_title = models.CharField(max_length=250)
    little_genie_description = HTMLField()

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse_lazy("core:view_about", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse_lazy("core:update_about", kwargs={"pk": self.pk})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]


class Gallery(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    title = models.CharField(max_length=250)
    image = VersatileImageField("Image", upload_to="images/Gallery")

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse_lazy("core:view_gallery", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse_lazy("core:update_gallery", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("core:delete_gallery", kwargs={"pk": self.pk})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]


class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    child_name = models.CharField(max_length=250)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=30)
    message = models.TextField(blank=True, null=True)
    is_checked = models.BooleanField(default=False)
    timestamp = models.DateTimeField(db_index=True, auto_now_add=True)

    def __str__(self):
        return str(self.child_name)

    def get_absolute_url(self):
        return reverse_lazy("core:view_contact", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse_lazy("core:update_contact", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("core:delete_contact", kwargs={"pk": self.pk})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]


class Feature(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    title = models.CharField(max_length=250)
    image = VersatileImageField("Image")
    description = models.TextField()

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse_lazy("core:view_feature", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse_lazy("core:update_feature", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("core:delete_feature", kwargs={"pk": self.pk})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]


class Social(models.Model):
    order = models.IntegerField(unique=True)
    icon = models.FileField(upload_to="images/SocialMediaIcons")
    link = models.URLField(max_length=200)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ("order",)
        verbose_name = "Social Media"
        verbose_name_plural = "Social Medias"

    def __str__(self):
        return str(self.link)

    def get_absolute_url(self):
        return reverse_lazy("core:view_social", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse_lazy("core:update_social", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("core:delete_social", kwargs={"pk": self.pk})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]


class FAQ(models.Model):
    question = models.CharField(max_length=350)
    answer = models.TextField()

    def __str__(self):
        return str(self.question)

    def get_absolute_url(self):
        return reverse_lazy("core:view_faq", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse_lazy("core:update_faq", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("core:delete_faq", kwargs={"pk": self.pk})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]
