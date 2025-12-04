from django.urls import path
from rest_framework.generics import ListAPIView
from teams.models import Team

from .serializers import TeamSerializer


app_name = "teams"

urlpatterns = [path("", ListAPIView.as_view(queryset=Team.objects.all(), serializer_class=TeamSerializer))]
