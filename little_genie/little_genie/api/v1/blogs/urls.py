from blogs.models import Blog
from django.urls import path
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView

from .serializers import BlogSerializer


app_name = "blogs"

urlpatterns = [
    path("", ListAPIView.as_view(queryset=Blog.objects.filter(is_published=True), serializer_class=BlogSerializer)),
    path(
        "<str:pk>/",
        RetrieveAPIView.as_view(queryset=Blog.objects.filter(is_published=True), serializer_class=BlogSerializer),
    ),
]
