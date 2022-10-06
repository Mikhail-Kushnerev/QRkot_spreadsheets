# QRkot_spreadseets

API приложения для Благотворительного фонда поддержки котиков.
Его назначение — сбор и распределение пожертвований между различными проектами

## Описание

Фонд собирает пожертвования на различные целевые проекты:
- на медицинское обслуживание нуждающихся хвостатых;
- на обустройство кошачьей колонии в подвале;
- на корм оставшимся без попечения кошкам — на любые цели;
- связанные с поддержкой кошачьей популяции.

## Содержание

- [Технологии](#технологии)
- [Использование](#использование)
- [REST API](#rest-api)
- [Над проектом работали](#над-проектом-работали)

## Технологии

- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](http://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [FastAPI Users](https://fastapi-users.github.io/fastapi-users/)
- [Google Cloud Platform](https://cloud.google.com/)
- [Google Sheets API](https://developers.google.com/sheets/api)
- [Google Drive API](https://developers.google.com/drive)
- [Uvicorn](https://www.uvicorn.org/)

## Использование

Склонируйте репозиторий  
Создайте виртуальное окружение 

```python
python -m venv venv
```

Активируйте виртуальное окружение  
Установите зависимости

```python
pip install -r requirements.txt
```

Отредактируйте и переименуйте  `.env.template`. в  `.env`  
Примените миграции

```python
alembic upgrade head
```

Запустите сервер из корневой папки проекта

```python
uvicorn app.main:app --reload
```

При первом запуске приложения будет создан суперюзер, с регистрационными данными из `.env`  

## REST API

Документация и web интервейс API будет доступен по адресу: http://localhost:8000/docs

## Над проектом работали

[Mikhail Kushnerev](https://github.com/Mikhail-Kushnerev)
