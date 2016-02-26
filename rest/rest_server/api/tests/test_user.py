"""
Test file for the user api
"""

"""
imports
"""

from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

"""
begin tests
"""

class UserTests(APITestCase):
    def test_create_user(self):
        """
        Make sure we can create a user
        """

        #post request
        url = reverse('register-user')
        data = {'username': 'ywarezk', 'first_name': 'Yariv', 'last_name': 'Katz', 'password': '12345678', 'email': 'no@no.no'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)

        #other requests are forbidden
        data = {'username': 'ywarezk', 'first_name': 'Yariv', 'last_name': 'Katz', 'password': '12345678', 'email': 'no@no.no'}
        response = self.client.put(url + '/1', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        response = self.client.delete(url + '/1', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_login(self):
        """
        test the login api
        """

        #post request
        url = reverse('register-user')
        data = {'username': 'ywarezk', 'first_name': 'Yariv', 'last_name': 'Katz', 'password': '12345678', 'email': 'no@no.no'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)

        #post request
        url = reverse('login-user')
        data = {'username': 'ywarezk', 'password': '12345678'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data)




