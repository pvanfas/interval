from django.urls import path

from . import views

app_name = "web"


urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("littlegenie/", views.LittleGenieView.as_view(), name="littlegenie"),
    path("foundation/", views.FoundationView.as_view(), name="foundation"),
    path("thanks/", views.ThanksView.as_view(), name="thanks"),
]
