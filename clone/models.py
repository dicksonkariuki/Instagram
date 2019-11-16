from django.db import models

class Profile(modesls.Model):
    profile_photo =models.ImageField(upload_to ='profile/')
    bio =models.CharField()