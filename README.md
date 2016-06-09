
#Monoku-test


# Prerequisites 
- [virtualenv](https://virtualenv.pypa.io/en/latest/)

# Initialize the project
Create and activate a virtualenv:

```bash
virtualenv env --no-site-packages --distribute -p /usr/local/bin/python3
or
pyvenv env
source env/bin/activate
```
Install dependencies:

```bash
pip install -r requirements.txt
```

Initialize the git repository

```bash
git init
git remote add origin git@github.com:/Monoku-test.git
```

Migrate, create a superuser, and run the server:

```bash
python national_planning/manage.py migrate
python national_planning/manage.py createsuperuser
python national_planning/manage.py runserver
```

Generate API docs:

```bash
npm install apidoc -g
python national_planning/manage.py apidoc 
```
