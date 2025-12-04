from products.models import OfferProduct
from products.models import Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_category(self, obj):
        return obj.category.name


class OfferProductSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    off_percent = serializers.CharField(source="get_off_percent")

    class Meta:
        depth = 1
        model = OfferProduct
        fields = "__all__"

    def get_name(self, obj):
        return obj.product.name
