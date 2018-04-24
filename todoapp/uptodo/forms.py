from django.forms import ModelForm

from uptodo.models import TodoTask


class TodoTaskForm(ModelForm):
    class Meta:
        model = TodoTask
        fields = ('task', 'due_date', 'title', 'status')
