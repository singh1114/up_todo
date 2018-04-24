import arrow

from django.db import models


class SoftDeletionModel(models.Model):
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True
