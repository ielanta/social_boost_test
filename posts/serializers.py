import logging

from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def create(self, validated_data):
        logging.info(f'Post by {validated_data["user"].username}: {validated_data["text"]}')
        return Post.objects.create(**validated_data)

    class Meta:
        model = Post
        fields = ['user', 'text', 'created_at']
