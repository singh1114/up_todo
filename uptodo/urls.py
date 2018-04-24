from django.conf.urls import url, include
from uptodo.api.api import TodoResource


urlpatterns = [
    url(r'^todo/?', include(TodoResource().urls), name='todores'),
]
