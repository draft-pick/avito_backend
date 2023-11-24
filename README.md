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

```
docker-compose up -d
```

3. Для пересборки контейнеров выполните команду:

```
sudo docker-compose up -d --build
```

4. В контейнере backend выполните миграции:

```
sudo docker-compose exec backend python manage.py migrate
```

Проект запущен и доступен по адресу: http://localhost:8000
