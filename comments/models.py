from django.db import models
from core.models import TimeStampedModel


class Comments(TimeStampedModel):

    class Meta:
        ordering = ("-created",)

    comment = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="comments", on_delete=models.CASCADE)
    resource = models.ForeignKey(
        "resources.Resources", related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.comment} - {self.resource}"
