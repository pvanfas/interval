import uuid

from django.db import models
from django.urls import reverse_lazy
from tinymce.models import HTMLField
from versatileimagefield.fields import VersatileImageField


class Author(models.Model):
    name = models.CharField(max_length=128)
    designation = models.CharField(max_length=250)
    email = models.EmailField(blank=True, null=True)
    photo = models.ImageField(upload_to="images/authors")
    about = models.TextField()

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse_lazy("blogs:view_author", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse_lazy("blogs:update_author", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("blogs:delete_author", kwargs={"pk": self.pk})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]


class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    title = models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    photo = VersatileImageField("Image", upload_to="images/Blog")
    published_date = models.DateField("published date(yyyy-mm-dd)")
    published_time = models.TimeField("published time(hh:mm:ss)")
    summary = models.TextField()
    content = HTMLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse_lazy("blogs:view_blog", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse_lazy("blogs:update_blog", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("blogs:delete_blog", kwargs={"pk": self.pk})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]
