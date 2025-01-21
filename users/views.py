from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from users.models import User
from users.serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    """Представление для создания нового объекта модели User."""

    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        """Сохраняет сериализованные данные при регистрации пользователя и хэширует пароль."""
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(ListAPIView):
    """Представление для создания нового объекта модели User."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated & IsAdminUser,)
