import arrow

from django.test import TestCase
from django.urls import reverse

from tastypie.test import ResourceTestCaseMixin

from uptodo.factories import TaskFactory


class TestTodoResource(ResourceTestCaseMixin, TestCase):
    def test_todo_resource(self):
        """
        test todo resource api endpoints
        """
        todotask = TaskFactory()
        response = self.api_client.get('/todo/task/', format='json')
        self.assertValidJSONResponse(response)
        self.assertKeys(self.deserialize(response)['objects'][0],
                        ('due_date', 'resource_uri', 'status', 'title'))
