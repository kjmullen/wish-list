from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase
from lists.models import List, ListItem
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class TestListCreateList(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="test",
                                             email="",
                                             password="password")
        self.list = List.objects.create(name="testlist",
                                        expiration_date="2016-04-25",
                                        user=self.user)

    def test_create_list(self):
        token = Token.objects.get(user_id=self.user.id)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        url = reverse('list_list')
        data = {"name":"test list", "expiration_date":"2016-05-01"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(List.objects.count(), 2)
        self.assertEqual(data['name'], "test list")


class TestListItemCreateList(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="test",
                                             email="",
                                             password="password")

        self.list = List.objects.create(name="testlist",
                                        expiration_date="2016-04-25",
                                        user=self.user)

        self.item = ListItem.objects.create(list=self.list,
                                            name="testitem",
                                            price=100,
                                            amazon_link="http://www.amazon.com")

    def test_create_list_item(self):
        token = Token.objects.get(user_id=self.user.id)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        url = reverse('list_list_item')
        data = {"list":self.list.id, "name":"apitest", "price":1100,
                "amazon_link":"http://www.amazon.com"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ListItem.objects.count(), 2)
        self.assertEqual(data['name'], "apitest")

