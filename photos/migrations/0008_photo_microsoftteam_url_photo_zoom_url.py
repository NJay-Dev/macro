# Generated by Django 4.2.5 on 2023-09-24 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0007_alter_category_id_alter_photo_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='microsoftTeam_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='zoom_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
