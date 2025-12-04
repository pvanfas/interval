from django.urls import path

from . import views

app_name = "main"

urlpatterns = [
    path("test/", views.test, name="test"),
    path("classtests/", views.ClassTestListView.as_view(), name="test_list"),
    path("classtests/create/", views.ClassTestCreateView.as_view(), name="test_create"),
    path("classtests/detail/<str:pk>/", views.ClassTestDetailView.as_view(), name="test_detail"),
    path("classtests/update/<str:pk>/", views.ClassTestUpdateView.as_view(), name="test_update"),
    path("classtests/delete/<str:pk>/", views.ClassTestDeleteView.as_view(), name="test_delete"),
]
