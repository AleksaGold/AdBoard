from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)

from advertisement.models import Advertisement, Review
from advertisement.serializers import AdvertisementSerializer, ReviewSerializer, ReviewDetailSerializer, \
    AdvertisementDetailSerializer


class AdvertisementCreateAPIView(CreateAPIView):
    """Представление для создания объекта модели Advertisement."""

    serializer_class = AdvertisementSerializer


class AdvertisementListAPIView(ListAPIView):
    """Представление для просмотра списка объектов модели Advertisement."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer


class AdvertisementRetrieveAPIView(RetrieveAPIView):
    """Представление для просмотра одного объекта модели Advertisement."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementDetailSerializer


class AdvertisementUpdateAPIView(UpdateAPIView):
    """Представление для обновления объекта модели Advertisement."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer


class AdvertisementDestroyAPIView(DestroyAPIView):
    """Представление для удаления объекта модели Advertisement."""

    queryset = Advertisement.objects.all()


class ReviewCreateAPIView(CreateAPIView):
    """Представление для создания объекта модели Review."""

    serializer_class = ReviewSerializer


class ReviewListAPIView(ListAPIView):
    """Представление для просмотра списка объектов модели Review."""

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewRetrieveAPIView(RetrieveAPIView):
    """Представление для просмотра одного объекта модели Review."""

    queryset = Review.objects.all()
    serializer_class = ReviewDetailSerializer


class ReviewUpdateAPIView(UpdateAPIView):
    """Представление для обновления объекта модели Review."""

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDestroyAPIView(DestroyAPIView):
    """Представление для удаления объекта модели Review."""

    queryset = Review.objects.all()
