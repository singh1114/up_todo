from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic.edit import FormView

from uptodo.constants import TemplateName
from uptodo.forms import SearchTaskForm, TodoTaskForm
from uptodo.handlers.todo_handlers import TodoHandler


class TaskView(FormView):
    form_class = TodoTaskForm

    def get(self, request, pk='', *args, **kwargs):
        """
        get the tasks using this Method
        """
        form_response = TodoHandler().get_initials(pk, self.form_class)
        return render(request, TemplateName.TODO_TASK, {
            'form': form_response, 'pk': pk})

    def post(self, request, pk='', *args, **kwargs):
        """
        post the tasks using this method
        handles both CreateView and UpdateView
        """
        if self.form_class(request.POST).is_valid():
            TodoHandler().handle_task_post(request, pk)
        if not pk:
            pk = ''
        return HttpResponseRedirect(reverse('tasks', kwargs = {'pk': pk}))

class DeleteTask(View):
    def get(self, request, pk, *args, **kwargs):
        TodoHandler().delete_task(pk)
        return HttpResponseRedirect(reverse('index'))


class SearchTasks(FormView):
    form_class = SearchTaskForm

    def get(self, request, *args, **kwargs):
        return render(request, TemplateName.SEARCH_TASK, {
            'form': self.form_class})

    def post(self, request, *args, **kwarsgs):
        if self.form_class(request.POST).is_valid():
            result = TodoHandler().search_tasks(request.POST['title'])
            objects = result['objects']
            return render(request, TemplateName.SEARCH_RESULTS, {
                'objects': objects})


class FilterTasks(FormView):
    form_class = SearchTaskForm

    def get(self, request, *args, **kwargs):
        return render(request, TemplateName.SEARCH_TASK, {
            'form': self.form_class})

    def post(self, request, *args, **kwarsgs):
        if self.form_class(request.POST).is_valid():
            result = TodoHandler().search_tasks(request.POST['title'])
            objects = result['objects']
            return render(request, TemplateName.SEARCH_RESULTS, {
                'objects': objects})
