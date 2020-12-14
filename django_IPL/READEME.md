# Setup project and run with following steps
## Install virtual environment
```sudo apt install python-virtualenv```

## Setup virtual environment with python 3.6+
```virtualenv venv -p python3```

## Install python dependencies
```pip install -r requirements.txt```

## Migrate database
```python manage.py migrate```

## Run server
```python manage.py runserver 8000```

## Test on browser
http://localhost:8000

# start page
http://localhost:8000/Home

#Loading data from csv

http://localhost:8000/load
