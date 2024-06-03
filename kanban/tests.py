from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from kanban.models import Task
import json
from django.urls import reverse
from rest_framework import status

class TaskTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

        self.task1 = Task.objects.create(title='Task 1', description='##### 1 description #####', user=self.user)
        self.task2 = Task.objects.create(title='Task 2', description='##### 2 description #####', user=self.user)
        
    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
    
    # def test_kanbanpage(self):
        # print('Title: ', self.task1.title + ' ' + 'Description: ',self.task1.description)
        # print('Title: ', self.task2.title + ' ' + 'Description: ',self.task2.description)
        
    def test_list_tasks(self):
        response = self.client.get('/tasks/')
        # self.assertEqual(response.status_code, 200)
        # print(len(response.data))
        # print(response.content.decode('utf-8'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        
        # print(json.dumps(response.data))
        
        
    def test_retrieve_task(self):
        response = self.client.get(reverse('task-detail', kwargs={'pk': self.task1.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Task 1')
        
    def test_bulk_update_tasks(self):
        data = [
            {'id': self.task1.id, 'title': 'Updated Task 1'},
            {'id': self.task2.id, 'title': 'Updated Task 2'},
        ]
        response = self.client.put(reverse('task-bulk-update'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.get(id=self.task1.id).title, 'Updated Task 1')
        self.assertEqual(Task.objects.get(id=self.task2.id).title, 'Updated Task 2')
        # print('##################################################')
        # print(json.dumps(response.data))
    
    def tearDown(self):
        self.user.delete()
        self.token.delete()



