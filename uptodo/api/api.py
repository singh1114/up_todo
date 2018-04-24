from tastypie.resources import ModelResource
from tastypie.constants import ALL

from uptodo.models import TodoTask


class CustomModelResource(ModelResource):
    def apply_filters(self, request, applicable_filters):
        """
        An ORM-specific implementation of ``apply_filters``.

        The default simply applies the ``applicable_filters`` as ``**kwargs``,
        but should make it possible to do more advanced things.
        """
        positive_filters = {}
        negative_filters = {}
        for lookup in applicable_filters.keys():
            if lookup.endswith( '__not_eq' ):
                negative_filters[ lookup ] = applicable_filters[ lookup ]
            else:
                positive_filters[ lookup ] = applicable_filters[ lookup ]

        return self.get_object_list(request).filter(**positive_filters).exclude(**negative_filters)


class TodoResource(CustomModelResource):
    class Meta:
        queryset = TodoTask.objects.all()
        resource_name = 'task'
        fields = ['title', 'due_date', 'status']
        filtering = {
            'title': ALL,
            'due_date': ['in', '__not_eq']
        }
