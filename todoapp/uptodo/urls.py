from django.conf.urls import url, include
from django.views.generic import TemplateView

from uptodo.api.api import TodoResource
from uptodo.constants import TemplateName
from uptodo.views import DeleteTask, FilterTasks, SearchTasks, TaskView


urlpatterns = [
    url(r'^todo/?', include(TodoResource().urls)),
    url(r'^tasks/(?P<pk>\d+)?$', TaskView.as_view(), name='tasks'),
    url(r'^index/?', TemplateView.as_view(template_name=TemplateName.INDEX),
        name='index'),
    url(r'^delete-task/(?P<pk>\d+)$', DeleteTask.as_view(),
        name='delete-task'),
    url(r'^search/?', SearchTasks.as_view(), name='search'),
    url(r'^filter/(?P<string>\w+)$', FilterTasks.as_view(),
        name='filter'),
    url(r'^filter-option/?', TemplateView.as_view(
        template_name=TemplateName.FILTER_OPTIONS), name='filter-option'),
]
