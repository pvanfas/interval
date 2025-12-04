from django.urls import path

from . import views

app_name = "api_users"

urlpatterns = [
    path("login/", views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", views.TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", views.RegisterView.as_view(), name="auth_register"),
]
