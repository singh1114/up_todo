# up_todo
API development using tastypie

# Installation

- `pip install -r requirements.txt`

- `sudo apt-get install redis-server`

- `redis-server`

- `python manage.py migrate`

**For running celery periodic tasks(Not in prod)**

- `celery -A todoapp worker -l info -B`
