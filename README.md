<h1>TheBlog - Новостной сайт.</h1>
<hr>
<br>

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

<ul type="1">Вариант использование SQLite.
    <ul>
      <li>клонируйте проект и создайте виртуальное окружение</li>
      <li>pip install -r requirements.txt</li>
      <li>в файле env.dev установить значение DEBUG на True</li>
    </ul>
    <ul>Выполните миграции:
        <li>в bash python manage.py makemigrations --noinput && python manage.py migrate</li>
        <li>в powershell python manage.py makemigrations --noinput ; python manage.py migrate</li>
    </ul>
  <ul>Создайте суперпользователя:</ul>
    <li>python manage.py createsuperuser</li>
    <ul>Запустите сервер:</ul>
    <li>python manage.py runserver</li>
    <li>Сервер будет доступен по адресу : http://127.0.0.1:8000/</li>
</ul>

<ul type="2">Вариант использование Postgres & Docker
      <li>клонируйте проект.</li>
      <li>в консоле введите команду docker-compose up -d --build</li>
      <ul>Создайте суперпользователя.
        <li>docker exec -it  blog python manage.py createsuperuser</li>
      </ul>
      <li>Сервер будет доступен по адресу : http://127.0.0.1:8000/</li>

</ul>
