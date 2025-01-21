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
def admin():
    """Фикстура для создания экземпляра тестового пользователя с ролью "admin"."""
    return User.objects.create(
        email="admin@test.com",
        first_name="test_first",
        last_name="test_last",
        role="admin",
        password="123teST",
    )


@pytest.fixture
def user_advertisement_db(user):
    """Фикстура для создания экземпляра тестового объявления, созданного пользователем с ролью "user"."""
    return Advertisement.objects.create(
        title="Test User Advertisement",
        price=100,
        author=user,
    )


@pytest.fixture
def admin_advertisement_db(admin):
    """Фикстура для создания экземпляра тестового объявления, созданного пользователем с ролью "admin"."""
    return Advertisement.objects.create(
        title="Test Admin Advertisement",
        price=100,
        author=admin,
    )


@pytest.fixture
def user_review_db(user, user_advertisement_db):
    """Фикстура для создания экземпляра тестового отзыва, созданного пользователем с ролью "user"."""
    return Review.objects.create(
        text="Test User Review",
        ad=user_advertisement_db,
        author=user,
    )


@pytest.fixture
def admin_review_db(admin, admin_advertisement_db):
    """Фикстура для создания экземпляра тестового отзыва, созданного пользователем с ролью "admin"."""
    return Review.objects.create(
        text="Test Admin Review",
        ad=admin_advertisement_db,
        author=admin,
    )
