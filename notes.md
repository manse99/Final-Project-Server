0.) `pip install -r requirements.txt` install all dependnecies in requirements.txt

1.) `mkvirtualenv ga` / ` workon ga`

2.) `django-admin startproject ga .`

3.) `pip install django`

4.) `pip freeze > requirements.txt`

5.)  `touch create-database.sql ` and add:

    CREATE DATABASE readme;

    CREATE USER server_admin WITH PASSWORD '1234'

    GRANT ALL PRIVILEDGES ON DATABASE ga TO ga_admin;



6.) `psq -f create-database.sql ` To create sq database from the command line 