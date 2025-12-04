from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView as TokenObtainPair
from rest_framework_simplejwt.views import TokenRefreshView as TokenRefresh

from users.models import CustomUser as User

from . import serializers


class TokenObtainPairView(TokenObtainPair):
    permission_classes = [AllowAny]
    serializer_class = serializers.UserTokenObtainPairSerializer


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = serializers.RegisterSerializer


class TokenRefreshView(TokenRefresh):
    pass
