<h1>TheBlog - Новостной сайт.</h1>
<hr>
<br>

<h1>инструменты:</h1>
<hr>
python >= 3.11
Django >= 4.2.4
Docker
Postgres(Для докер контейнера)

<h3>Функционал</h3>
- Возможность создавать посты(только для администрации)
- Сортировка новостей по категориям, добавление категорий.(только для администрации)
- Создание и редактирование аккаунта
- Созданеие и изменения профиля пользователя(с ссылками на соц сети и изображением)
- Возможность ставить лайки(только для зарегистрированных пользователей)
- Просмотр профиля автора поста.
- Добавление комментариев к посту.



<h3>Старт</h3>
1. Вариант использование SQLite.
  - клонируйте проект и создайте виртуальное окружение
  - pip install -r requirements.txt
  - в файле env.dev установить значение DEBUG на True
  Выполните миграции:
    - в bash python manage.py makemigrations --noinput && python manage.py migrate или в powershell python manage.py makemigrations --noinput ; python manage.py migrate
  Создайте суперпользователя:
    - python manage.py createsuperuser
Запустите сервер:
    - python manage.py runserver

Сервер будет доступен по адресу : http://127.0.0.1:8000/

2. Вариант использование Postgres & Docker
  - клонируйте проект.
  - в консоле введите команду docker-compose up -d --build
  Создайте суперпользователя.
  - docker exec -it  blog python manage.py createsuperuser

Сервер будет доступен по адресу : http://127.0.0.1:8000/
