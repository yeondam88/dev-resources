# Generated by Django 3.0.5 on 2020-04-12 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0004_resources_url'),
        ('comments', '0002_auto_20200408_0525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='resources.Resources'),
        ),
    ]
