from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from posts.models import Post


class PostListTests(APITestCase):
    url = reverse('post-list')

    def setUp(self):
        self.user = User.objects.create_user('user', 'Password')
        self.data = {'text': 'Test data'}

    def test_create_post_by_not_authorized(self):
        # check that not authorized user cannot create post
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_list_postst_by_user(self):
        self.client.force_authenticate(user=self.user)
        self.client.post(self.url, self.data)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['text'], self.data['text'])

    def test_create_post_by_user(self):
        self.client.force_authenticate(user=self.user)
        self.assertEqual(Post.objects.count(), 0)
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().text, self.data['text'])

