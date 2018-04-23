from django.db import models

from uptodo.choices import TaskStatus


class TodoTask(models.Model):
    task = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    due_date = models.DateField()
    title = models.CharField(max_length=3000)
    status = models.CharField(max_length=1, choices=TaskStatus.choices)
