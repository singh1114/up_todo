from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import FormView

from uptodo.constants import TemplateName
from uptodo.forms import TodoTaskForm
from uptodo.handlers.todo_handlers import TodoHandler


class TaskView(FormView):
    form_class = TodoTaskForm

    def get(self, request, pk='', *args, **kwargs):
        """
        get the tasks using this Method
        """
        form_response = TodoHandler().get_initials(pk, self.form_class)
        return render(request, TemplateName.TODO_TASK, {'form': form_response})

    def post(self, request, pk='', *args, **kwargs):
        """
        post the tasks using this method
        handles both CreateView and UpdateView
        """
        if self.form_class(request.POST).is_valid():
            TodoHandler().handle_task_post(request, pk)
        return HttpResponseRedirect(reverse('tasks', kwargs = {'pk': pk}))
