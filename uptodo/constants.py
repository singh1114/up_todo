from djchoices import DjangoChoices, ChoiceItem


class TaskStatus(DjangoChoices):
    pending = ChoiceItem("P")
    completed = ChoiceItem("C")
