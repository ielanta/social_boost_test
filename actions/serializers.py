import logging

from rest_framework import serializers
from actions.models import Like


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def create(self, validated_data):
        like, is_created = Like.objects.get_or_create(**validated_data)

        if is_created:
            logging.info(f'Like by {validated_data["user"].username} for post #{validated_data["post"].pk}')
        return like

    def delete(self, validated_data):
        like = Like.objects.get(**validated_data)

        if not like:
            logging.error(f'Like by {validated_data["user"].username} for post #{validated_data["post"].pk} '
                          f'does not exists')
        else:
            logging.info(f'Unlike by {validated_data["user"].username} for post #{validated_data["post"].pk}')
            like.delete()

    class Meta:
        model = Like
        fields = ['user', 'post', 'created_at']
