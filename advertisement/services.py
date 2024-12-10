from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAdminUser

from users.permissions import IsAdminPermission, IsAuthorPermission


def get_user_permissions(request):
    """Настройка прав доступа в зависимости от прав пользователя."""
    if not request.user.is_authenticated:
        raise PermissionDenied("Для выполнения этого запроса необходима авторизация")
    if request.user.is_superuser:
        return (IsAdminUser,)
    if request.user.role == "user":
        return (IsAuthorPermission(),)
    if request.user.role == "admin":
        return (IsAdminPermission(),)
