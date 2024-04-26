# tango_with_django
## Installation and Setup:
Install the latest python version and open up command prompt. To check your current Python version use: **python --version**

Now, before installing Django, we created a virtual environment for our project so that this Django settings do not apply to the whole system, just this virtual environment. 

**pip install virtualenvwrapper**
**mkvirtualenv django "__virtualenv-name__"**
(this will activate the virtualenv of the given name)

### Installing Django

**pip install django**
To check Django version:
**django-admin --version**

To create a project,
**django-admin startproject "__project_name__"**

To run a initial server:
**python manage.py runserver**