# Описание

REST API для социальной сети блогеров. Поддерживает CRUD для постов, групп, комментариев.

## Стек

```text
Django
Djangorestframework
Djangorestframework-simplejwt
```

## Схема апи

```text
schema.yaml в корне проекта
```

## Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone https://github.com/a-menshikov/api_final_yatube.git
```

```bash
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```bash
python3 -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

Выполнить миграции:

```bash
python3 manage.py migrate
```

Запустить проект:

```bash
python3 manage.py runserver
```
