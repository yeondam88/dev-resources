# Generated by Django 3.0.5 on 2020-04-06 06:24

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resources',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='resources', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='resources',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='resources',
            name='resource_type',
            field=models.CharField(blank=True, choices=[('blog_post', 'Blog Post'), ('youtube', 'Youtube'), ('website', 'Website'), ('book', 'Book')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='resources',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='title', unique=True, verbose_name='Resource Address'),
        ),
        migrations.AddField(
            model_name='resources',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='resources',
            name='thumbnail',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='resources',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
