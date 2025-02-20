
### AdBoard - Backend
Backend для сайта объявлений. Проект реализует функциональность для управления объявлениями, авторизации и аутентификации пользователей, а также отзывов к объявлениям.

### О проекте

**Технологии:**
- **Django:** Основной фреймворк для разработки.
- **Django REST Framework (DRF):** Для создания API.
- **PostgreSQL:** Используется в качестве базы данных.
- **CORS:** Настроено для взаимодействия с фронтенд-приложением.
- **Docker, Docker Compose**: Для контейнеризации и управления сервисами.
- **pytest:** для написания тестов.
- **Swagger:** для автоматической генерации документации API.


   
#### Проект написан с испoльзованием версии **Python 3.12**


### Функциональность

- Регистрация и аутентификация пользователей, сброс и восстановление пароля через почту.
- Поддержка ролей "Пользователь" и "Админ". Админы имеют полные права на редактирование и удаление любых объявлений. Пользователи могут управлять только своими объявлениями.
- Управление объявлениями и отзывами: чтение, создание, редактирование, удаление. 
- Поиск объявлений по названию через заголовок сайта.


### Установка и настройка


#### Клонируйте репозиторий:
```
git@github.com:AleksaGold/AdBoard.git
```
#### Установите зависимости:
Для запуска проекта и установки зависимостей вам необходимо создать виртуальное окружение, сделать это можно с помощью команды
```
poetry install
```

#### Настройте базу данных в settings.py и выполните миграции:
```
python manage.py migrate
```

#### Настройка переменных окружения:
Создайте файл `.env` в корне проекта и заполните его переменными окружения указанными в файле `.env.sample`.


### CORS
CORS настроен для взаимодействия с фронтендом:

- Разрешён доступ с определённых доменов.
- Используется библиотека **django-cors-headers**.

### Запуск через Docker Compose
Для запуска всех сервисов выполните команду:
```
docker-compose up --build
```
Добавьте флаг -d, чтобы запустить в фоновом режиме:
```
docker-compose up -d
```
После запуска доступность сервисов можно проверить командой:
```
docker-compose ps
```
#### Состав `docker-compose.yaml`
Файл docker-compose.yaml описывает следующие сервисы:
- **db**: PostgreSQL для хранения данных приложения.
- **app**: Контейнер с Django-приложением: выполняет HTTP-запросы к API.

### Тестирование
Запуск тестов с помощью `pytest`:
```
pytest
```
### Доступ к Swagger
Для интеграции Swagger в проект используется библиотека **drf-spectacular**.
После запуска сервера документация доступна по следующему пути:
http://127.0.0.1:8000/api/docs/
