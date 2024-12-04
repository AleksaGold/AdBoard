from rest_framework.serializers import ModelSerializer

from advertisement.models import Advertisement, Review


class AdvertisementSerializer(ModelSerializer):
    """Сериализатор для модели Advertisement."""

    class Meta:
        model = Advertisement
        fields = (
            "id",
            "title",
            "price",
            "description",
            "author",
            "created_at",
        )


class ReviewSerializer(ModelSerializer):
    """Сериализатор для модели Review."""

    class Meta:
        model = Review
        fields = (
            "id",
            "text",
            "author",
            "ad",
        )


class ReviewDetailSerializer(ModelSerializer):
    """Сериализатор для одного объекта Review."""

    ad = AdvertisementSerializer(read_only=True)

    class Meta:
        model = Review
        fields = (
            "id",
            "author",
            "text",
            "ad",
        )


class AdvertisementDetailSerializer(ModelSerializer):
    """Сериализатор для одного объекта Advertisement."""

    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Advertisement
        fields = (
            "id",
            "title",
            "price",
            "description",
            "author",
            "created_at",
            "reviews",
        )
