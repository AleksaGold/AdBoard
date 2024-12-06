from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from advertisement.models import Advertisement, Review
from advertisement.serializers import (AdvertisementDetailSerializer,
                                       AdvertisementSerializer,
                                       ReviewDetailSerializer,
                                       ReviewSerializer)
from users.permissions import IsAuthorPermission, IsAdminPermission


class AdvertisementCreateAPIView(CreateAPIView):
    """Представление для создания объекта модели Advertisement."""

    serializer_class = AdvertisementSerializer

    def perform_create(self, serializer):
        """Переопределение метода для автоматической привязки владельца к создаваемому объекту."""
        serializer.save(author=self.request.user)


class AdvertisementListAPIView(ListAPIView):
    """Представление для просмотра списка объектов модели Advertisement."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = (AllowAny,)
    filterset_fields = ('title',)


class AdvertisementRetrieveAPIView(RetrieveAPIView):
    """Представление для просмотра одного объекта модели Advertisement."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementDetailSerializer


class AdvertisementUpdateAPIView(UpdateAPIView):
    """Представление для обновления объекта модели Advertisement."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = (IsAuthenticated & IsAuthorPermission | IsAdminPermission | IsAdminUser,)


class AdvertisementDestroyAPIView(DestroyAPIView):
    """Представление для удаления объекта модели Advertisement."""

    queryset = Advertisement.objects.all()
    permission_classes = (IsAuthenticated & IsAuthorPermission | IsAdminPermission | IsAdminUser,)


class ReviewCreateAPIView(CreateAPIView):
    """Представление для создания объекта модели Review."""

    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        """Переопределение метода для автоматической привязки владельца к создаваемому объекту."""
        serializer.save(author=self.request.user)


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
    permission_classes = (IsAuthenticated & IsAuthorPermission | IsAdminPermission | IsAdminUser,)


class ReviewDestroyAPIView(DestroyAPIView):
    """Представление для удаления объекта модели Review."""

    queryset = Review.objects.all()
    permission_classes = (IsAuthenticated & IsAuthorPermission | IsAdminPermission | IsAdminUser,)
