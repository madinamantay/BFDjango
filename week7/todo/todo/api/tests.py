from rest_framework.test import APITestCase


class TaskListTest(APITestCase):

    # noinspection DuplicatedCode
    def setUp(self):
        self.user = {
            'username': 'admin2',
            'password': 'admin1'
        }

        self.client.post('/auth/register/', self.user)
        self.client.login(username=self.user['username'], password=self.user['password'])

        self.task_list = {'name': 'test list'}
        self.client.post('/lists/', self.task_list)

    def test_list_task_list(self):
        response = self.client.get('/lists/')

        self.assertEqual(response.status_code, 200)

        task_list = response.data

        self.assertIsNotNone(task_list)
        self.assertEqual(self.task_list['name'], task_list[0].get('name'))

    def test_create_task_list(self):
        self.client.login(username=self.user['username'], password=self.user['password'])

        task_list = {'name': 'test list'}
        response = self.client.post('/lists/', task_list)

        self.assertEqual(response.status_code, 201)

        data = response.data

        self.assertEqual(data.get('name'), task_list['name'])
        self.assertEqual(data.get('owner').get('username'), self.user['username'])

    def test_create_blank_task_list(self):
        self.client.login(username=self.user['username'], password=self.user['password'])

        task_list = {'name': ''}
        response = self.client.post('/lists/', task_list)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.get('name')[0], 'This field may not be blank.')

    def test_create_unauthorized_task_list(self):
        self.client.logout()

        task_list = {'name': 'test list'}
        response = self.client.post('/lists/', task_list)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data.get('detail'), 'Authentication credentials were not provided.')

    def test_retrieve_task_list(self):
        _id = 1
        response = self.client.get(f'/lists/{_id}/')

        self.assertEqual(response.status_code, 200)
        task_list = response.data

        self.assertIsNotNone(task_list)
        self.assertEqual(self.task_list['name'], task_list.get('name'))

    def test_retrieve_404_task_list(self):
        _id = 2
        response = self.client.get(f'/lists/{_id}/')

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data['detail'], 'Not found.')

    def test_update_task_list(self):
        _id = 1
        task_list = {'name': 'updated test list'}
        response = self.client.put(f'/lists/{_id}/', task_list)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], task_list['name'])

    def test_update_blank_task_list(self):
        _id = 1
        task_list = {'name': ''}
        response = self.client.put(f'/lists/{_id}/', task_list)

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.get('name')[0], 'This field may not be blank.')

    def test_update_404_task_list(self):
        _id = 2
        task_list = {'name': ''}
        response = self.client.put(f'/lists/{_id}/', task_list)

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data['detail'], 'Not found.')

    def test_delete_task_list(self):
        _id = 1
        response = self.client.delete(f'/lists/{_id}/')

        self.assertEqual(response.status_code, 204)

    def test_delete_404_task_list(self):
        _id = 2
        response = self.client.delete(f'/lists/{_id}/')

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data['detail'], 'Not found.')


class ToDoTest(APITestCase):

    # noinspection DuplicatedCode
    def setUp(self):
        self.user = {
            'username': 'admin2',
            'password': 'admin1'
        }

        self.client.post('/auth/register/', self.user)
        self.client.login(username=self.user['username'], password=self.user['password'])

        self.task_list = {'name': 'test list'}
        self.client.post('/lists/', self.task_list)

    def test_list_tasks(self):
        _id = 1
        response = self.client.get(f'/lists/{_id}/task/')

        self.assertEqual(response.status_code, 200)
        items = response.data

        self.assertIsNotNone(items)
        self.assertEqual(len(items), 0)

    def test_create_tasks(self):
        self.client.login(username=self.user['username'], password=self.user['password'])

        _id = 1
        task = {'name': 'test todo'}
        response = self.client.post(f'/lists/{_id}/task/', task)

        self.assertEqual(response.status_code, 201)
        created_task = response.data

        self.assertIsNotNone(created_task)
        self.assertEqual(created_task.get('name'), 'test task')

        response = self.client.get(f'/lists/{_id}/task/', task)

        self.assertEqual(response.status_code, 200)
        items = response.data

        self.assertIsNotNone(items)
        self.assertEqual(len(items), 1)

        item = items[0]

        self.assertIsNotNone(item)
        self.assertEqual(item.get('name'), 'test task')
