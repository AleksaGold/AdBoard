from django.urls import path
from djoser.views import UserViewSet
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserListAPIView

app_name = UsersConfig.name

urlpatterns = [
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
    path("users/", UserListAPIView.as_view(), name="users_list"),
    path(
        "reset_password/",
        UserViewSet.as_view({"post": "reset_password"}),
        name="reset_password",
    ),
    path(
        "reset_password_confirm/",
        UserViewSet.as_view({"post": "reset_password_confirm"}),
        name="reset_password_confirm",
    ),
]
