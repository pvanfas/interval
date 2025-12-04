import uuid

from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse_lazy
from versatileimagefield.fields import VersatileImageField


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse_lazy("products:view_category", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse_lazy("products:update_category", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("products:delete_category", kwargs={"pk": self.pk})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    photo = VersatileImageField("Image", upload_to="images/Products")
    rating = models.DecimalField(
        max_digits=2, decimal_places=1, default=4.5, validators=[MaxValueValidator(5), MinValueValidator(0.5)]
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.TextField()
    is_hotproduct = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse_lazy("products:view_product", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse_lazy("products:update_product", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("products:delete_product", kwargs={"pk": self.pk})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]


class OfferProduct(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    offer_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    offer_startdate = models.DateField()
    offer_enddate = models.DateField()

    def __str__(self):
        return str(self.product)

    def get_off_percent(self):
        return round((100 * (self.product.price - self.offer_price) / self.product.price), 2)

    def get_absolute_url(self):
        return reverse_lazy("products:view_offer_product", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse_lazy("products:update_offer_product", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("products:delete_offer_product", kwargs={"pk": self.pk})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]


class ProductEnquiry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    name = models.CharField(max_length=250)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=30)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    message = models.TextField()
    is_checked = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse_lazy("products:view_product_enquiry", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse_lazy("products:update_product_enquiry", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse_lazy("products:delete_product_enquiry", kwargs={"pk": self.pk})

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]
