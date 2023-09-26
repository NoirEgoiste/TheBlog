<h1>TheBlog - Новостной сайт.</h1>
<br>
<img src="https://github.com/NoirEgoiste/TheBlog/blob/main/static/mini_blog/images/blog_pic.png">
<h1>инструменты:</h1>
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
Перед началом работы переименуйте .env.example в .env
<h3>Вариант использование Postgres & Docker</h3> 
<ul>
     <li>клонируйте проект.</li>
     <li>в консоле введите команду docker-compose up -d --build</li>
     <li>docker exec -it  blog python manage.py createsuperuser</li>
     <li>Сервер будет доступен по адресу : http://127.0.0.1:8000/</li>
</ul>
<h3>Вариант использование SQLite.</h3>

* клонируйте проект и создайте виртуальное окружение
* pip install -r requirements.txt
* в файле env.dev установить значение DEBUG на True
* Выполните миграции:
     - в bash python manage.py makemigrations --noinput && python manage.py migrate
     - в powershell python manage.py makemigrations --noinput ; python manage.py migrate
* Создайте суперпользователя:
    - python manage.py createsuperuser
    - Запустите сервер:
    - python manage.py runserver
    - Сервер будет доступен по адресу : http://127.0.0.1:8000/
<br>
<h1>Страница поста</h1>
<img src="https://github.com/NoirEgoiste/TheBlog/blob/main/static/mini_blog/images/post_pic.png">
<br>

<br>
<h1>Автор поста</h1>
<img src="https://github.com/NoirEgoiste/TheBlog/blob/main/static/mini_blog/images/profile_author_pic.png">
<br>
