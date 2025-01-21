from django.urls import path

from advertisement.apps import AdvertisementConfig
from advertisement.views import (AdvertisementCreateAPIView,
                                 AdvertisementDestroyAPIView,
                                 AdvertisementListAPIView,
                                 AdvertisementRetrieveAPIView,
                                 AdvertisementUpdateAPIView,
                                 ReviewCreateAPIView, ReviewDestroyAPIView,
                                 ReviewListAPIView, ReviewRetrieveAPIView,
                                 ReviewUpdateAPIView)

app_name = AdvertisementConfig.name

urlpatterns = [
    path(
        "advertisements/create/",
        AdvertisementCreateAPIView.as_view(),
        name="advertisements_create",
    ),
    path(
        "advertisements/",
        AdvertisementListAPIView.as_view(),
        name="advertisements_list",
    ),
    path(
        "advertisements/retrieve/<int:pk>/",
        AdvertisementRetrieveAPIView.as_view(),
        name="advertisements_retrieve",
    ),
    path(
        "advertisements/update/<int:pk>/",
        AdvertisementUpdateAPIView.as_view(),
        name="advertisements_update",
    ),
    path(
        "advertisements/destroy/<int:pk>/",
        AdvertisementDestroyAPIView.as_view(),
        name="advertisements_destroy",
    ),
    path("reviews/create/", ReviewCreateAPIView.as_view(), name="reviews_create"),
    path("reviews/", ReviewListAPIView.as_view(), name="reviews_list"),
    path(
        "reviews/retrieve/<int:pk>/",
        ReviewRetrieveAPIView.as_view(),
        name="reviews_retrieve",
    ),
    path(
        "reviews/update/<int:pk>/", ReviewUpdateAPIView.as_view(), name="reviews_update"
    ),
    path(
        "reviews/destroy/<int:pk>/",
        ReviewDestroyAPIView.as_view(),
        name="reviews_destroy",
    ),
]
