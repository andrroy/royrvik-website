### My personal website

*Disclaimer*: A lot of the code in this repo is pretty badly written. This is my own personal project, where functionality has been prioritized before anything else. 


### Setup

```
virtualenv env
source env
cp example_settings.py pwebsite/pwebsite/settings.py
python manage.py syncdb
python manage.py runserver
```

To active crontabs

```
python manage.py crontab add
```

To deactive

```
python manage.py crontab remove
```