<h1>TheBlog - Новостной сайт.</h1>
<hr>
<br>

<h1>инструменты:</h1>
<hr>
python >= 3.11<br>
Django >= 4.2.4<br>
Docker<br>
Postgres(Для докер контейнера)<br>

<h3>Функционал</h3>
- Возможность создавать посты(только для администрации)<br>
- Сортировка новостей по категориям, добавление категорий.(только для администрации)<br>
- Создание и редактирование аккаунта<br>
- Созданеие и изменения профиля пользователя(с ссылками на соц сети и изображением)<br>
- Возможность ставить лайки(только для зарегистрированных пользователей)<br>
- Просмотр профиля автора поста.<br>
- Добавление комментариев к посту.<br>



<h3>Старт</h3>
1. Вариант использование SQLite.
<ul>
  <li>клонируйте проект и создайте виртуальное окружение</li>
  <li>pip install -r requirements.txt</li>
  <li>в файле env.dev установить значение DEBUG на True</li>
</ul>
  Выполните миграции:
    - в bash python manage.py makemigrations --noinput && python manage.py migrate или в powershell python manage.py makemigrations --noinput ; python manage.py migrate
  Создайте суперпользователя:
    - python manage.py createsuperuser
Запустите сервер:
    - python manage.py runserver
Сервер будет доступен по адресу : http://127.0.0.1:8000/
</ul>
2. Вариант использование Postgres & Docker
  - клонируйте проект.
  - в консоле введите команду docker-compose up -d --build
  Создайте суперпользователя.
  - docker exec -it  blog python manage.py createsuperuser

Сервер будет доступен по адресу : http://127.0.0.1:8000/
