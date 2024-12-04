from django.db import models
from django.contrib.auth.models import User
from photos.models import Category
from django.utils import timezone
# Create your models here.

#Broker access
class BrokerAccess(models.Model):
    password = models.CharField(max_length=255, unique=True)


#Broker File details
class Broker(models.Model):
    class Meta:
        verbose_name = 'Broker'
        verbose_name_plural = 'Broker'
    
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=False, blank=False)
    video = models.FileField(upload_to="videos/", null=True, blank=True)
    website_url = models.CharField(max_length=2000, null=True, blank=True)
    whatsapp_number = models.CharField(max_length=20, null=True, blank=True)
    facebook_url = models.CharField(max_length=2000, null=True, blank=True)
    location = models.CharField(max_length=1000, blank=True, null=True)
    zoom_url = models.CharField(max_length=2000, null=True, blank=True)
    microsoftTeam_url = models.CharField(max_length=2000, null=True, blank=True)
    twitter_url = models.CharField(max_length=2000, null=True, blank=True)
    playstore_url = models.CharField(max_length=2000, null=True, blank=True)
    linkedin_url = models.CharField(max_length=2000, null=True, blank=True)
    instagram_url = models.CharField(max_length=2000, null=True, blank=True)
    pinterest_url = models.CharField(max_length=2000, null=True, blank=True)
    youtube_url = models.CharField(max_length=2000, null=True, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    

    def __str__(self):
        return self.description
