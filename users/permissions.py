from rest_framework import permissions


class IsAuthorPermission(permissions.BasePermission):
    """Проверка прав доступа для владельцев."""

    def has_object_permission(self, request, view, obj):
        """Проверяет является ли пользователь владельцем."""
        return obj.author == request.user


class IsAdminPermission(permissions.BasePermission):
    """Проверка прав доступа для пользователей с ролью "admin"."""

    def has_permission(self, request, view):
        """Проверяет роль пользователя."""
        return request.user.role == "ADMIN"
