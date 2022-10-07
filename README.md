# small todo application to test out Django 4

If you want to use a virtual environment with django try out pipenv:

1. Install Python
2. Install Pycharm
3. Mkdir \<Projectfolder>
4. Install pip
5. Install pipenv
6. Set PATH for pipenv
7. cd into projectfolder

```sh
8. pipenv install django
```

=> with that command..

- a pipfile (and lockfile) is created. (like package.(lock).json, and..
- a virtual environment is build, to be precise a new folder at:
  "C:\Users\\'User'\\.virtualenvs\\{nameOfProject}-ID"
  ..that serves as the virtualenv with django inside.

With the command..

```sh
pipenv --venv
```

..you get the full path to that directory

```sh
9. pipenv shell
```

=> activates the virtualenv so that it ll will use the python interpreter inside this virtualenv, NOT the one that you have installed globally on your machine. in other words: it launches a subshell in the virtual env.

```sh
10. django-admin startproject <projectfolder> .
```

=> take notice of the period at the end, so that the project is installed in the current directory!

11. finally run the server:

```sh
python manage.py runserver
```

optionally add the port number:

```sh
python manage.py runserver 9000
```

..in case the default port (8000) is already in use

12. Ready! Now you can create new modules:

```sh
python manage.py startapp <nameOfTheModule>
```

Have fun! :)
