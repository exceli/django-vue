from unittest import TestCase

from rest_framework.test import APIClient


class PersonAPIViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/api/v1/form/'

    def test_create_person(self):
        data = {
            'name': 'Test_person',
            'age': 30,
        }
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name'], data['name'])
        self.assertEqual(response.data['age'], data['age'])

    def test_create_person_with_invalid_data(self):
        data = {
            'name': 'Invalid',
            'age': 'Invalid_age',
        }

        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 400)
        self.assertIn('age', response.data)

    def test_get_all_persons(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)