from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'

    GENDER_CHOICES = (
        (GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female'),
    )

    JOB_TITLES = (
        ('software engineer', 'Software Engineer'),
        ('frontend engineer', 'Front End Engineer'),
        ('backend engineer', 'Back End Engineer'),
        ('graphic designer', 'Graphic Designer'),
        ('ux designer', 'UX Designer'),
    )

    avatar = models.ImageField(null=True, blank=True, upload_to="avatars")
    gender = models.CharField(max_length=10, null=True,
                              choices=GENDER_CHOICES, blank=True)
    job_title = models.CharField(
        max_length=20, null=True, choices=JOB_TITLES, blank=True)
    bio = models.TextField(default='', blank=True)
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default="", blank=True)

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name
