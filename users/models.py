from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'

    GENDER_CHOICES = (
        (GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female'),
    )

    JOB_TITLES = (
        ('software_engineer', 'Software Engineer'),
        ('frontend_engineer', 'Front End Engineer'),
        ('backend_engineer', 'Back End Engineer'),
        ('graphic_designer', 'Graphic Designer'),
        ('ux_designer', 'UX Designer'),
    )

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True,
                              choices=GENDER_CHOICES, blank=True)
    job_title = models.CharField(
        max_length=20, null=True, choices=JOB_TITLES, blank=True)
    bio = models.TextField(default='', blank=True)
