from rest_framework import serializers
from resources.models import Resources
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)


class ResoucesSerializer(serializers.ModelSerializer):

    tags = TagListSerializerField()

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
        )
