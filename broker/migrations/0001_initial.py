# Generated by Django 4.2.4 on 2023-09-01 15:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('photos', '0007_alter_category_id_alter_photo_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Broker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('website_url', models.CharField(blank=True, max_length=200, null=True)),
                ('whatsapp_number', models.CharField(blank=True, max_length=20, null=True)),
                ('facebook_url', models.CharField(blank=True, max_length=200, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('twitter_url', models.CharField(blank=True, max_length=200, null=True)),
                ('playstore_url', models.CharField(blank=True, max_length=200, null=True)),
                ('linkedin_url', models.CharField(blank=True, max_length=200, null=True)),
                ('instagram_url', models.CharField(blank=True, max_length=200, null=True)),
                ('pinterest_url', models.CharField(blank=True, max_length=200, null=True)),
                ('youtube_url', models.CharField(blank=True, max_length=200, null=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='photos.category')),
            ],
            options={
                'verbose_name': 'Broker',
                'verbose_name_plural': 'Broker',
            },
        ),
    ]
