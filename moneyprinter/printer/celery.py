import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moneyprinter.settings")

app = Celery('printer')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'get_coins_30s': {
        'task': 'printer.tasks.get_coins',
        'schedule': 30.0
    }
}

app.autodiscover_tasks()