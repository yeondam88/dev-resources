from django.db import models
from . import managers


class TimeStampedModel(models.Model):

    """ Abstract Model to extend to other models """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = managers.CustomModelManager()

    class Meta:
        # Create model but not commit to DB
        abstract = True
