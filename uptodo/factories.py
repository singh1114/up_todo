import arrow

from factory.django import DjangoModelFactory

from factory import Sequence
from factory.fuzzy import FuzzyText

from uptodo.choices import TaskStatus
from uptodo.models import TodoTask


class TaskFactory(DjangoModelFactory):
    """
    Create factories for the purpose of testing
    """
    class Meta:
        model = TodoTask

    due_date = arrow.utcnow().shift(days=10).date()
    title = FuzzyText(length=200)
    status = TaskStatus.pending
