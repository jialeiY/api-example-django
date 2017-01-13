# drchrono birthday reminder
send email to patients for happy birthday!
- active or inactive the service
- set email sending time
- edit email subject and email text

### Requirements
- [pip](https://pip.pypa.io/en/stable/)
- [python virtual env](https://packaging.python.org/installing/#creating-and-using-virtual-environments)
- [RabbitMQ 3.6.6 Windows](https://www.rabbitmq.com/download.html)
- [celery 3.1.25] (http://docs.celeryproject.org/en/3.1/django/index.html)

### Setup
``` bash
$ pip install -r requirements.txt
$ python manage.py runserver
```
in new window
``` bash
$ celery -A drchrono worker -l info
```
in new window
``` bash
$ celery -A drchrono beat
```
`social_auth_drchrono/` contains a custom provider for [Python Social Auth](http://psa.matiasaguirre.net/) that handles OAUTH for drchrono. To configure it, set these fields in your `drchrono/settings.py` file:

```
SOCIAL_AUTH_DRCHRONO_KEY
SOCIAL_AUTH_DRCHRONO_SECRET
SOCIAL_AUTH_DRCHRONO_SCOPE
LOGIN_REDIRECT_URL
```
