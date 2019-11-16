from django.db import models

class Profile(modesls.Model):
    profile_photo =models.ImageField(upload_to ='profile/')
    bio =models.CharField()

class Image(models.Model):
    image =models.ImageField(upload_to='image/')
    image_name=models.CharField(max_length=30)
    image_caption=models.CharField()
    profile=models.ForeignKey(Profile,on_delete=models.cascade)
    likes=models.ManytoManyField(likes)
    comments=models.TextField()