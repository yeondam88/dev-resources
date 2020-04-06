from django.db import models


class TimeStampedModel(models.Model):

    """ Abstract Model to extend to other models """

    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        # Create model but not commit to DB
        abstract = True
