from django.urls import path
from products.models import OfferProduct
from products.models import Product
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView

from .serializers import OfferProductSerializer
from .serializers import ProductSerializer


app_name = "products"

urlpatterns = [
    path("", ListAPIView.as_view(queryset=Product.objects.all(), serializer_class=ProductSerializer)),
    path("offers/", ListAPIView.as_view(queryset=OfferProduct.objects.all(), serializer_class=OfferProductSerializer)),
    path("<str:pk>/", RetrieveAPIView.as_view(queryset=Product.objects.all(), serializer_class=ProductSerializer)),
]
