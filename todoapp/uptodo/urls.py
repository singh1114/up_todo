from django.conf.urls import url, include
from uptodo.api.api import TodoResource
from uptodo.views import TaskView


urlpatterns = [
    url(r'^todo/?', include(TodoResource().urls), name='todores'),
    url(r'^tasks/(?P<pk>\d+)?$', TaskView.as_view(), name='tasks')
]
