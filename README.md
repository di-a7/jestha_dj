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

# open shell
python manage.py shell

# import
from app_name.folder_name.file_name import model/function

# create 
model_name.objects.create(field1 = "....", field2="...", ....)

# get all data in the model
model_name.objects.all()

# Single data fetch
a = model_name.objects.get(id = 1)

# Updata exisiting data
a.field1 = "new value"
a.save()

# delete data
a.delete()

# filter data
model_name.objects.filter(field1 = "value", field2="value",....)

# .gitignore file, git and github