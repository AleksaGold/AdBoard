from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

from users.permissions import IsAdminPermission, IsAuthorPermission


def get_user_permissions(request):
    """Настройка прав доступа в зависимости от прав пользователя."""
    if not request.user.is_authenticated:
        return (IsAuthenticatedOrReadOnly(),)
    if request.user.is_superuser:
        return (IsAdminUser(),)
    if request.user.role == "user":
        return (IsAuthorPermission(),)
    if request.user.role == "admin":
        return (IsAdminPermission(),)
