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


# .gitignore file, git and github