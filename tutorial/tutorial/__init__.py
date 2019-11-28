from __future__ import absolute_import

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
import time

from .celery import app as celery_app
from .celery import task_wait
from celery.result import AsyncResult
#x=task_wait.delay()
#while x.state=='PENDING':
#    time.sleep(2)
#    print(x.state)

#print(x.task_id)
#res=AsyncResult(x.task_id)
#res.ready()
#print("hello")
