from django import forms
from django.forms import ModelForm

from uptodo.models import TodoTask


class TodoTaskForm(ModelForm):
    class Meta:
        model = TodoTask
        fields = ('task', 'due_date', 'title', 'status')


class SearchTaskForm(forms.Form):
    title = forms.CharField(max_length=3000)
