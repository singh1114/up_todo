from base.handlers.form_handlers import FormHandler

from uptodo.dbio import TodoTaskDbIO


class TodoHandler:
    def get_initials(self, pk, form_class):
        if not pk:
            return form_class
        todo_task = TodoTaskDbIO().get_object({'pk': pk})
        return FormHandler().load_initials(form_class, todo_task)
