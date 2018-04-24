from base.dbio import AbstractDbIO

from uptodo.models import TodoTask


class TodoTaskDbIO(AbstractDbIO):
    def __init__(self):
        self.model = TodoTask
