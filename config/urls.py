from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("djoser.urls")),
    path("advertisement/", include("advertisement.urls", namespace="advertisement")),
    path("user/", include("users.urls", namespace="user")),
]
