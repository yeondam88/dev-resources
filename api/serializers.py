from rest_framework import serializers
from users.models import User
from resources.models import Resources
from comments.models import Comments
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', )

class CommentSerialzier(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Comments
        exclude = ('id',)

class ResoucesSerializer(serializers.ModelSerializer):

    tags = TagListSerializerField()
    comments = CommentSerialzier(many=True, read_only=True)

    class Meta:
        model = Resources
        fields = (
            'id',
            'title',
            'author',
            'description',
            'tags',
            'resource_type',
            'thumbnail',
            'slug',
            'url',
            'comments',
        )