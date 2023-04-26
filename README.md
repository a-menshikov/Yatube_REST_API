# Финальное задание 9 спринта.

## Описание

REST API для социальной сети блогеров. Поддерживает CRUD для постов, групп, комментариев.

### Стек:
```
Django
Djangorestframework
Djangorestframework-simplejwt
```
### Схема апи:
```
schema.yaml в корне проекта
```



### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/a-menshikov/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
