from rest_framework import serializers
from resources.models import Resources
from comments.models import Comments
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)


class CommentSerialzier(serializers.ModelSerialzier):

    class Meta:
        model = Comments
        fields = '__all__'

class ResoucesSerializer(serializers.ModelSerializer):

    tags = TagListSerializerField()
    comments = CommentSerialzier()

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