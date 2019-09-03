from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from posts.models import Post
from activity.models import Like


class LikeListTests(APITestCase):
    url = reverse('my-like-list')

    def setUp(self):
        self.user = User.objects.create_user('user', 'Password')
        post = Post.objects.create(text='Test', user=self.user)
        self.data = {'post': post.pk}

    def test_create_like_by_not_authorized(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_list_likes_by_user(self):
        self.client.force_authenticate(user=self.user)
        self.client.post(self.url, self.data)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['post'], self.data['post'])

    def test_create_like_by_user(self):
        self.client.force_authenticate(user=self.user)
        self.assertEqual(Like.objects.count(), 0)
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Like.objects.count(), 1)
        self.assertEqual(Like.objects.get().user.pk, self.user.pk)


class DeleteLikeTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user('user', 'Password')
        post = Post.objects.create(text='Test', user=self.user)
        like = Like.objects.create(post=post, user=self.user)
        self.url = reverse('delete-my-like', kwargs={'pk': like.pk})

    def test_delete_like_by_not_authorized(self):
        response = self.client.delete(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_like_by_user(self):
        self.client.force_authenticate(user=self.user)
        self.assertEqual(Like.objects.count(), 1)
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Like.objects.count(), 0)


