# Generated by Django 3.0.5 on 2020-04-15 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_auto_20200412_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='replies', to='comments.Comments'),
        ),
    ]