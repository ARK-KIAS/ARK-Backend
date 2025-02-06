![GithubCI](https://github.com/ARK-KIAS/ARK-Backend/actions/workflows/deploy.yml/badge.svg)

# FastAPI application support #2

Проект демонстрация организации проекта FastAPI с использованием паттерна Repository.

- FastAPI
- SqlAlchemy
- Postgres
- Alembic
- Docker

---

## Запуск с Docker через Makefile _(в прод)_
### 1. Старт с Docker
```shell
docker-compose up --build
```

### 2. Alembic migrate
Не выключая контейнеры выполнить команду
```shell
docker exec -it app-net-back alembic upgrade head
```

> [!NOTE]
> Документация будет доступна по адресу [http:\\\127.0.0.1:9000\docs](http:\\127.0.0.1:9000\docs)

---

## Запуск без Docker _(локально)_:
### Virtualenv
```shell
python -m venv venv
```
- Linux / MacOS
```shell
venv/bin/activate
```
- Windows
```shell
python venv\Scripts\activate
```

### Установка poetry (не обязательно)
```shell
pip install poetry
```
### Установка зависимостей
```shell
poetry install
```
или
```shell
pip install -r requirements.txt
```

### База данных
В файл `.env` прописать свои настройки Postgres

### Alembic migrate
```shell
alembic upgrade head
```

### Старт
```shell
python main.py
```

### Перейти по адресу
```shell
http:\\127.0.0.1:8000\docs
```
