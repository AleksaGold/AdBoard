import pytest
from django.urls import reverse
from rest_framework import status

from advertisement.models import Advertisement, Review


@pytest.mark.django_db
def test_advertisement_create(user, client):
    """Тестирование создания объявления."""
    client.force_authenticate(user=user)
    url = reverse("advertisement:advertisements_create")
    data = {
        "title": "Test Advertisement",
        "price": 100,
        "author": user.id,
    }
    response = client.post(url, data)

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["title"] == "Test Advertisement"


@pytest.mark.django_db
def test_advertisement_list(user, client, advertisement_db):
    """Тестирование просмотра списка объявлений."""
    client.force_authenticate(user=user)
    url = reverse("advertisement:advertisements_list")

    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data["results"]) == 1


@pytest.mark.django_db
def test_advertisement_retrieve(user, client, advertisement_db):
    """Тестирование просмотра одного объявления."""
    client.force_authenticate(user=user)
    url = reverse("advertisement:advertisements_retrieve", args=(advertisement_db.id,))

    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data["title"] == "Test Advertisement"


@pytest.mark.django_db
def test_advertisement_update(user, client, advertisement_db):
    """Тестирование обновления объявления."""
    client.force_authenticate(user=user)
    url = reverse("advertisement:advertisements_update", args=(advertisement_db.id,))
    data = {"title": "New Advertisement"}

    response = client.patch(url, data)

    assert response.status_code == status.HTTP_200_OK
    assert response.data["title"] == "New Advertisement"


@pytest.mark.django_db
def test_advertisement_destroy(user, client, advertisement_db):
    """Тестирование удаления объявления."""
    client.force_authenticate(user=user)
    url = reverse("advertisement:advertisements_destroy", args=(advertisement_db.id,))

    response = client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Advertisement.objects.filter(id=advertisement_db.id).exists() is False


@pytest.mark.django_db
def test_review_create(user, client, advertisement_db):
    """Тестирование создания отзыва."""
    client.force_authenticate(user=user)
    url = reverse("advertisement:reviews_create")
    data = {
        "text": "Test Review",
        "ad": advertisement_db.id,
        "author": user.id,
    }
    response = client.post(url, data)

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["ad"] == advertisement_db.id


@pytest.mark.django_db
def test_review_list(user, client, review_db):
    """Тестирование просмотра списка отзывов."""
    client.force_authenticate(user=user)
    url = reverse("advertisement:reviews_list")

    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1


@pytest.mark.django_db
def test_review_retrieve(user, client, review_db):
    """Тестирование просмотра одного отзыва."""
    client.force_authenticate(user=user)
    url = reverse("advertisement:reviews_retrieve", args=(review_db.id,))

    response = client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert Review.objects.filter(id=review_db.id).exists() is True


@pytest.mark.django_db
def test_review_update(user, client, review_db, advertisement_db):
    """Тестирование обновления отзыва."""
    client.force_authenticate(user=user)
    url = reverse("advertisement:reviews_update", args=(review_db.id,))
    data = {"text": "New Review", "ad": advertisement_db.id, "author": user.id}

    response = client.put(url, data)

    assert response.status_code == status.HTTP_200_OK
    assert response.data["author"] == user.id


@pytest.mark.django_db
def test_review_destroy(user, client, review_db):
    """Тестирование удаления отзыва."""
    client.force_authenticate(user=user)
    url = reverse("advertisement:reviews_destroy", args=(review_db.id,))

    response = client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Review.objects.count() == 0
