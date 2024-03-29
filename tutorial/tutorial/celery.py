from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
import time

# set the default Django settings module for the 'celery' program.


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tutorial.settings')
app = Celery('tutorial')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


@app.task(bind=True)
def task_wait(self,seconds=20):
    time.sleep(seconds)
    return 'done'
    #print('Request: {0!r}'.format(self.request))