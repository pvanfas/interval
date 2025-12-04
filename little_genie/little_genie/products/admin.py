from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from products.models import Category
from products.models import OfferProduct
from products.models import Product
from products.models import ProductEnquiry


@admin.register(Category)
class CategoryAdmin(ImportExportActionModelAdmin):
    list_display = ("name",)


@admin.register(Product)
class ProductAdmin(ImportExportActionModelAdmin):
    list_display = ("category", "price", "name", "description")


@admin.register(OfferProduct)
class OfferProductAdmin(ImportExportActionModelAdmin):
    list_display = ("product", "offer_price", "offer_startdate", "offer_enddate")


@admin.register(ProductEnquiry)
class ProductEnquiryAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "email", "phone", "product", "message", "timestamp")
