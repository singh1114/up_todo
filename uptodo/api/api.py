from tastypie.resources import ModelResource
from tastypie.constants import ALL

from uptodo.models import TodoTask


class TodoResource(ModelResource):
    class Meta:
        queryset = TodoTask.objects.all()
        resource_name = 'task'
        fields = ('title', 'due_date', 'status')
        filtering = {
            'title': ALL,
            ''
        }
