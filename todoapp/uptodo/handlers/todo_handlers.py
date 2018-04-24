from base.handlers.form_handlers import FormHandler
from django.http import HttpResponseServerError

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
