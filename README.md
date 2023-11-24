# avito_backend

avito_backend - сервис динамического сегментирования пользователей с возможностью экспорта истории попадания/выбывания пользователя из сегмента в формат csv

# Технологии

* Python
* DRF
* Docker-compose

# Установка

Для запуска приложения проделайте следующие шаги:

1. Склонируйте репозиторий.

```
git clone https://github.com/draft-pick/avito_backend.git
```

2. Перейти в папку с проектом

```
cd avito_backend/backend
```

3. Запустите проект:

```
docker-compose up -d
```

4. В контейнере backend выполните миграции:

```
sudo docker-compose exec backend python manage.py migrate
```

Проект запущен и доступен по адресу: http://localhost:8000

# Примеры запросов

* POST запрос на добавление новых сегментов: /api/segments/
  ```
  {
    "title": "segment1",
    "slug": "segment-1"
  }
  ```
* POST запрос на создание нового пользователя: /api/users/
  ```
  {
    "nickname": "1000",
  }
  ```
* GET запрос на получение списка пользователей: /api/users/
* GET запрос на получение пользователя: /api/users/${id}/
* GET запрос на получение истории попадания/выбывания пользователя из сегмента: /api/users/${id}/date-filter/
* GET запрос на получение истории попадания/выбывания пользователя из сегмента за ноябрь: /api/users/${id}/date-filter/?date_time_after=2023-11-01&date_time_before=2023-11-30
* GET запрос на экпорт истории попадания/выбывания пользователя из сегмента за ноябрь в формате csv: /api/users/${id}/download-csv/?date_time_after=2023-11-01&date_time_before=2023-11-30
* GET запрос на получение списка сегментов: /api/segments/
* GET запрос на получение сегмента: /api/segments/${slug}/
* PUT запрос на изменение сегмента: /api/segments/${slug}/
  ```
  {
      "title": "segment2",
      "slug": "segment-2"
  }
  ```
* PUT запрос на изменения пользователя: /api/segments/${slug}/
  ```
  {
      "nickname": "user123",
      "segments": [
          "segment2"
      ]
  }
  ```
* DELETE запрос на удаление сегмента: /api/segments/${slug}/
* DELETE запрос на удаление пользователя: /api/users/${id}/


