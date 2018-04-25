from __future__ import absolute_import, unicode_literals

import arrow

from celery import task

from uptodo.dbio import TodoTaskDbIO

@task
def auto_delete():
    cut_off = arrow.utcnow().shift(days=-30).datetime
    tasks = TodoTaskDbIO().filter_objects({'deleted_at__lte': cut_off})
    tasks.delete()
