# install virtual environment
pip install virtualenv

# create virtual environment
virtualenv env 

# activate virtual environment
venv\Scripts\activate(win)
source env/Scripts/activate (linux/mac)

# to create new project
django-admin startproject project_name . ['.' is optional]

# to run django server
python manage.py runserver

# create app
python manage.py startapp app_name

# create migration file
python manage.py makemigrations

# create tables in db
python manage.py migrate

# create superuser
python manage.py createsuperuser

# .gitignore file, git and github