import arrow

import requests

from django.urls import reverse
from django.http import HttpResponseServerError

from base.handlers.form_handlers import FormHandler

from django.conf import settings

from uptodo.dbio import TodoTaskDbIO


class TodoHandler:
    def get_initials(self, pk, form_class):
        if not pk:
            return form_class
        todo_task = TodoTaskDbIO().get_object({'pk': pk})
        return FormHandler().load_initials(form_class, todo_task)

    def handle_task_post(self, request, pk):
        """
        handle task posting
        """
        parent_task_pk = request.POST['task']
        if parent_task_pk:
            parent_task = TodoTaskDbIO().get_object({'pk': parent_task_pk})
        parent_task = None
        data_dict = {
            'task': parent_task,
            'due_date': request.POST['due_date'],
            'title': request.POST['title'],
            'status': request.POST['status']
        }
        if pk:
            todo_task = TodoTaskDbIO().get_object({'pk': pk})
            if todo_task:
                TodoTaskDbIO().update_object(todo_task, data_dict)
                return
            return HttpResponseServerError()
        TodoTaskDbIO().create_object(data_dict)
        return

    def delete_task(self, pk):
        TodoTaskDbIO().delete_object({'pk': pk})

    def search_tasks(self, title):
        response = requests.get(settings.BASE_URL +
            '/todo/task/?format=json&title__icontains={}'.format(title))
        return response.json()

    def filter_tasks(self, string):
        if string == 'today':
            today = arrow.utcnow().format('YYYY-MM-DD')
            response = requests.get(settings.BASE_URL +
                '/todo/task/?format=json&due_date={}'.format(today))
        if string == 'thisweek':
            week_last = arrow.utcnow().shift(days=-7).format('YYYY-MM-DD')
            week_first = arrow.utcnow().format('YYYY-MM-DD')
            response = requests.get(settings.BASE_URL +
                '/todo/task/?format=json&due_date__gte={}&due_date__lte={}'
                .format(week_last, week_first))
        if string == 'overdue':
            today = arrow.utcnow().format('YYYY-MM-DD')
            response = requests.get(settings.BASE_URL +
                '/todo/task/?format=json&due_date__lt={}&status=P'
                .format(today))
        return response.json()
