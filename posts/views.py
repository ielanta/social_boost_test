from rest_framework import generics

from posts.models import Post
from posts.serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    """
    List all posts, or create a new post.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

