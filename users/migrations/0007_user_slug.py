# Generated by Django 3.0.5 on 2020-04-19 03:50

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200412_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='username', unique=True, verbose_name='Username'),
        ),
    ]
