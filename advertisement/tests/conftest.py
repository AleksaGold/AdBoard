import pytest
from rest_framework.test import APIClient

from advertisement.models import Advertisement, Review
from users.models import User


@pytest.fixture
def client():
    """Фикстура для создания экземпляра тестового API-клиента."""
    return APIClient()


@pytest.fixture
def user():
    """Фикстура для создания экземпляра тестового пользователя."""
    return User.objects.create(
        email="user@test.com",
        first_name="test_first",
        last_name="test_last",
        role="user",
        password="123teST",
    )


@pytest.fixture
def advertisement_db(user):
    """Фикстура для создания экземпляра тестового объявления."""
    return Advertisement.objects.create(
        title="Test Advertisement",
        price=100,
        author=user,
    )


@pytest.fixture
def review_db(user, advertisement_db):
    """Фикстура для создания экземпляра тестового отзыва."""
    return Review.objects.create(
        text="Test Review",
        ad=advertisement_db,
        author=user,
    )
