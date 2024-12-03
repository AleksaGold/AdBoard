from django.db import models

from config import settings

NULLABLE = {"blank": True, "null": True}


class Advertisement(models.Model):
    """Класс для описания модели Advertisement."""

    title = models.CharField(max_length=100, verbose_name="Название товара")
    price = models.PositiveIntegerField(verbose_name="Цена товара")
    description = models.TextField(verbose_name="Описание товара", **NULLABLE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь, который создал объявление",
        related_name="advertisements",
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Время и дата создания объявления"
    )

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ("-created_at",)

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return f"{self.title} (от {self.author})"


class Review(models.Model):
    """Класс для описания модели Review."""

    text = models.TextField(verbose_name="Текст отзыва")
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Пользователь, который оставил отзыв",
        related_name="reviews",
    )
    ad = models.ForeignKey(
        "advertisement.Advertisement",
        on_delete=models.CASCADE,
        verbose_name="Объявление, под которым оставлен отзыв",
        related_name="reviews",
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Время и дата создания отзыва"
    )

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return f"Отзыв {self.author} для {self.ad}"
