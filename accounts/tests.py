from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from accounts.models import Account


class AccountListTests(APITestCase):
    url = reverse('account-list')

    def setUp(self):
        self.user = User.objects.create_user('user', 'Password')

    def test_create_post_by_not_authorized(self):
        # check that not authorized user cannot get account list
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_list_users_by_user(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class AccountCreateTests(APITestCase):
    url = reverse('account-registration')

    def setUp(self):
        self.data = {'email': 'steli@close.io', 'password': 'Leo12345!', 'username':'steli'}

    def test_create_valid_account(self):
        self.assertEqual(Account.objects.count(), 0)
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # check account info
        self.assertEqual(Account.objects.count(), 1)

        # check clearbit account info
        self.assertEqual(Account.objects.get().name, 'Steli Efti')
        self.assertEqual(Account.objects.get().bio, 'CEO of @close')
        self.assertEqual(Account.objects.get().company_role, 'leadership')
        self.assertEqual(Account.objects.get().facebook, 'steliefti')

    def test_create_invalid_account(self):
        # risky email
        self.data = {'email': 'alex@clearbit.com', 'password': 'Leo12345!', 'username': 'alex'}
        self.assertEqual(Account.objects.count(), 0)
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)




