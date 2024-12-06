from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    """Кастомная реализация пагинации."""

    page_size = 4
