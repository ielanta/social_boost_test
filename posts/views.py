from rest_framework import generics

from posts.models import Post
from posts.serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    """
    List all user's posts, or create a new post.
    """
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)
