from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    """Модель User для хранения информации о пользователях веб-приложения."""

    USER = "user"
    ADMIN = "admin"
    ROLES = [
        (USER, "Пользователь"),
        (ADMIN, "Администратор"),
    ]

    username = None
    email = models.EmailField(
        unique=True, verbose_name="Электронная почта пользователя (email)"
    )

    first_name = models.CharField(max_length=50, verbose_name="Имя пользователя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия пользователя")
    phone = PhoneNumberField(verbose_name="Телефон для связи", **NULLABLE)
    role = models.CharField(
        max_length=20,
        choices=ROLES,
        verbose_name="Роль пользователя",
        default="user",
    )
    image = models.ImageField(
        upload_to="users/avatars", verbose_name="Аватарка пользователя", **NULLABLE
    )
    token = models.CharField(max_length=100, verbose_name="Токен", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return f"{self.email} - {self.role}"
