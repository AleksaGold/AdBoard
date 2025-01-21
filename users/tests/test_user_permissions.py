import pytest
from django.urls import reverse
from rest_framework import status

from advertisement.models import Advertisement, Review


@pytest.mark.django_db
def test_unauthorized_advertisement_create(client):
    """Тестирование создания объявления неавторизованным пользователем.
    Создание объявления должно быть недоступно."""
    url = reverse("advertisement:advertisements_create")
    data = {"title": "Unauthorized Advertisement", "price": 100}
    response = client.post(url, data)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_unauthorized_advertisement_list(
    client, user_advertisement_db, admin_advertisement_db
):
    """Тестирование просмотра списка объявлений неавторизованным пользователем."""
    url = reverse("advertisement:advertisements_list")
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data["results"]) == 2


@pytest.mark.django_db
def test_admin_advertisement_retrieve(admin, client, user_advertisement_db):
    """Тестирование просмотра любого объявления администратором."""
    client.force_authenticate(user=admin)

    url = reverse(
        "advertisement:advertisements_retrieve", args=(user_advertisement_db.id,)
    )
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data["title"] == "Test User Advertisement"


@pytest.mark.django_db
def test_user_advertisement_retrieve(
    user, client, user_advertisement_db, admin_advertisement_db
):
    """Тестирование просмотра любого объявления пользователем."""
    client.force_authenticate(user=user)

    user_url = reverse(
        "advertisement:advertisements_retrieve", args=(user_advertisement_db.id,)
    )
    user_response = client.get(user_url)

    assert user_response.status_code == status.HTTP_200_OK
    assert user_response.data["title"] == "Test User Advertisement"

    admin_url = reverse(
        "advertisement:advertisements_retrieve", args=(admin_advertisement_db.id,)
    )
    admin_response = client.get(admin_url)

    assert admin_response.status_code == status.HTTP_200_OK
    assert admin_response.data["title"] == "Test Admin Advertisement"


@pytest.mark.django_db
def test_unauthorized_advertisement_retrieve(client, user_advertisement_db):
    """Тестирование просмотра объявления неавторизованным пользователем.
    Просмотр объявления должен быть недоступен."""
    url = reverse(
        "advertisement:advertisements_retrieve", args=(user_advertisement_db.id,)
    )
    response = client.get(url)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_admin_advertisement_update(admin, client, user_advertisement_db):
    """Тестирование обновления любого объявления администратором."""
    client.force_authenticate(user=admin)

    url = reverse(
        "advertisement:advertisements_update", args=(user_advertisement_db.id,)
    )
    data = {"title": "Change User Advertisement"}
    response = client.patch(url, data)

    assert response.status_code == status.HTTP_200_OK
    assert response.data["title"] == "Change User Advertisement"


@pytest.mark.django_db
def test_user_advertisement_update(
    user, client, user_advertisement_db, admin_advertisement_db
):
    """Тестирование обновления любого объявления пользователем.
    Обновление объявления созданного другим пользователем должно быть недоступно."""
    client.force_authenticate(user=user)

    user_url = reverse(
        "advertisement:advertisements_update", args=(user_advertisement_db.id,)
    )
    user_data = {"title": "Change User Advertisement"}
    user_response = client.patch(user_url, user_data)

    assert user_response.status_code == status.HTTP_200_OK
    assert user_response.data["title"] == "Change User Advertisement"

    admin_url = reverse(
        "advertisement:advertisements_update", args=(admin_advertisement_db.id,)
    )
    admin_data = {"title": "Change Admin Advertisement"}
    admin_response = client.patch(admin_url, admin_data)

    assert admin_response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_unauthorized_advertisement_update(client, user_advertisement_db):
    """Тестирование обновления объявления неавторизованным пользователем.
    Обновление объявления должно быть недоступно."""

    url = reverse(
        "advertisement:advertisements_update", args=(user_advertisement_db.id,)
    )
    data = {"text": "Change User Review"}
    response = client.patch(url, data)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_admin_advertisement_destroy(admin, client, user_advertisement_db):
    """Тестирование удаления любого объявления администратором."""
    client.force_authenticate(user=admin)

    url = reverse(
        "advertisement:advertisements_destroy", args=(user_advertisement_db.id,)
    )
    response = client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Advertisement.objects.filter(id=user_advertisement_db.id).exists() is False


@pytest.mark.django_db
def test_user_advertisement_destroy(
    user, client, user_advertisement_db, admin_advertisement_db
):
    """Тестирование удаления любого объявления пользователем.
    Удаление объявления созданного другим пользователем должно быть недоступно."""
    client.force_authenticate(user=user)

    user_url = reverse(
        "advertisement:advertisements_destroy", args=(user_advertisement_db.id,)
    )
    user_response = client.delete(user_url)

    assert user_response.status_code == status.HTTP_204_NO_CONTENT
    assert Advertisement.objects.filter(id=user_advertisement_db.id).exists() is False

    admin_url = reverse(
        "advertisement:advertisements_destroy", args=(admin_advertisement_db.id,)
    )
    admin_response = client.delete(admin_url)

    assert admin_response.status_code == status.HTTP_403_FORBIDDEN
    assert Advertisement.objects.filter(id=admin_advertisement_db.id).exists() is True


@pytest.mark.django_db
def test_unauthorized_advertisement_destroy(client, user_advertisement_db):
    """Тестирование удаления объявления неавторизованным пользователем.
    Удаление объявления должно быть недоступно."""

    url = reverse(
        "advertisement:advertisements_destroy", args=(user_advertisement_db.id,)
    )
    response = client.delete(url)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert Advertisement.objects.filter(id=user_advertisement_db.id).exists() is True


@pytest.mark.django_db
def test_unauthorized_review_create(client, user_advertisement_db):
    """Тестирование создания отзыва неавторизованным пользователем.
    Создание отзыва должно быть недоступно."""
    url = reverse("advertisement:reviews_create")
    data = {
        "text": "Unauthorized Review",
        "ad": user_advertisement_db.id,
    }
    response = client.post(url, data)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_unauthorized_review_list(client, user_review_db, admin_review_db):
    """Тестирование просмотра списка отзывов неавторизованным пользователем.
    Просмотр списка отзывов должен быть недоступен."""
    url = reverse("advertisement:reviews_list")
    response = client.get(url)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_admin_review_retrieve(admin, client, user_review_db):
    """Тестирование просмотра любого отзыва администратором."""
    client.force_authenticate(user=admin)

    url = reverse("advertisement:reviews_retrieve", args=(user_review_db.id,))
    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data["text"] == "Test User Review"


@pytest.mark.django_db
def test_user_review_retrieve(user, client, user_review_db, admin_review_db):
    """Тестирование просмотра любого отзыва пользователем."""
    client.force_authenticate(user=user)

    user_url = reverse("advertisement:reviews_retrieve", args=(user_review_db.id,))
    user_response = client.get(user_url)

    assert user_response.status_code == status.HTTP_200_OK
    assert user_response.data["text"] == "Test User Review"

    admin_url = reverse("advertisement:reviews_retrieve", args=(admin_review_db.id,))
    admin_response = client.get(admin_url)

    assert admin_response.status_code == status.HTTP_200_OK
    assert admin_response.data["text"] == "Test Admin Review"


@pytest.mark.django_db
def test_unauthorized_review_retrieve(client, user_review_db):
    """Тестирование просмотра отзыва неавторизованным пользователем.
    Просмотр отзыва должен быть недоступен."""
    url = reverse("advertisement:reviews_retrieve", args=(user_review_db.id,))
    response = client.get(url)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_admin_review_update(admin, client, user_review_db):
    """Тестирование обновления любого отзыва администратором."""
    client.force_authenticate(user=admin)

    url = reverse("advertisement:reviews_update", args=(user_review_db.id,))
    data = {"text": "Change User Review"}
    response = client.patch(url, data)

    assert response.status_code == status.HTTP_200_OK
    assert response.data["text"] == "Change User Review"


@pytest.mark.django_db
def test_user_review_update(user, client, user_review_db, admin_review_db):
    """Тестирование обновления любого отзыва пользователем.
    Обновление отзыва созданного другим пользователем должно быть недоступно."""
    client.force_authenticate(user=user)

    user_url = reverse("advertisement:reviews_update", args=(user_review_db.id,))
    user_data = {"text": "Change User Review"}
    user_response = client.patch(user_url, user_data)

    assert user_response.status_code == status.HTTP_200_OK
    assert user_response.data["text"] == "Change User Review"

    admin_url = reverse("advertisement:reviews_update", args=(admin_review_db.id,))
    admin_data = {"text": "Change Admin Review"}
    admin_response = client.patch(admin_url, admin_data)

    assert admin_response.status_code == status.HTTP_403_FORBIDDEN
    assert user_response.data["text"] != admin_data


@pytest.mark.django_db
def test_unauthorized_review_update(client, user_review_db):
    """Тестирование обновления отзыва неавторизованным пользователем.
    Обновление отзыва должно быть недоступно."""

    url = reverse("advertisement:reviews_update", args=(user_review_db.id,))
    data = {"text": "Change User Review"}
    response = client.patch(url, data)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_admin_review_destroy(admin, client, user_review_db):
    """Тестирование удаления любого отзыва администратором."""
    client.force_authenticate(user=admin)

    url = reverse("advertisement:reviews_destroy", args=(user_review_db.id,))
    response = client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Review.objects.filter(id=user_review_db.id).exists() is False


@pytest.mark.django_db
def test_user_review_destroy(user, client, user_review_db, admin_review_db):
    """Тестирование удаления любого отзыва пользователем.
    Удаление отзыва созданного другим пользователем должно быть недоступно."""
    client.force_authenticate(user=user)

    user_url = reverse("advertisement:reviews_destroy", args=(user_review_db.id,))
    user_response = client.delete(user_url)

    assert user_response.status_code == status.HTTP_204_NO_CONTENT
    assert Review.objects.filter(id=user_review_db.id).exists() is False

    admin_url = reverse("advertisement:reviews_destroy", args=(admin_review_db.id,))
    admin_response = client.delete(admin_url)

    assert admin_response.status_code == status.HTTP_403_FORBIDDEN
    assert Review.objects.filter(id=admin_review_db.id).exists() is True


@pytest.mark.django_db
def test_unauthorized_review_destroy(client, user_review_db):
    """Тестирование удаления отзыва неавторизованным пользователем.
    Удаление отзыва должно быть недоступно."""

    url = reverse("advertisement:reviews_destroy", args=(user_review_db.id,))
    response = client.delete(url)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert Review.objects.filter(id=user_review_db.id).exists() is True
