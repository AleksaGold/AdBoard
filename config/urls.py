from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("advertisement/", include("advertisement.urls", namespace="advertisement")),
    # path("users/", include("users.urls", namespace="users")),
]
