# Generated by Django 4.2.5 on 2023-09-24 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='broker',
            name='microsoftTeam_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='broker',
            name='zoom_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
