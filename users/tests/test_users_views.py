import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_user_create(client):
    """Тестирование создания пользователя."""
    url = reverse("users:register")
    data = {
        "email": "user@test.com",
        "first_name": "test_first",
        "last_name": "test_last",
        "role": "USER",
        "password": "123teST",
    }
    response = client.post(url, data)

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["email"] == "user@test.com"
