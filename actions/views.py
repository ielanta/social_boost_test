from rest_framework import generics

from actions.models import Like
from actions.serializers import LikeSerializer


class LikeList(generics.ListCreateAPIView):
    """
    List all user's likes, or create a new like.
    """
    serializer_class = LikeSerializer

    def get_queryset(self):
        return Like.objects.filter(user=self.request.user)


class DeleteLike(generics.DestroyAPIView):
    """
    Delete like
    """
    serializer_class = LikeSerializer

    def get_queryset(self):
        return Like.objects.filter(user=self.request.user)