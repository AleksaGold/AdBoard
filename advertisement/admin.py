from django.contrib import admin

from advertisement.models import Advertisement, Review


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    """Класс для настройки отображения модели "Advertisement" в административной панели"""

    list_display = (
        "pk",
        "title",
        "price",
        "description",
        "author",
        "created_at",
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Класс для настройки отображения модели "Review" в административной панели"""

    list_display = (
        "pk",
        "text",
        "author",
        "ad",
        "created_at",
    )
