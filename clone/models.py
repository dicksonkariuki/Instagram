from django.db import models
from django.contrib.auth.models import User
import datetime as dt

class Profile(models.Model):
    profile_photo =models.ImageField(upload_to ='profile/')
    bio =models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def save_profile(self):
        self.save()
    @classmethod
    def get_by_id(cls, id):
        details = Profile.objects.get(user = id)
        return details
    @classmethod
    def filter_by_id(cls, id):
        details = Profile.objects.filter(user = id).first()
        return details
     @classmethod
    def search_user(cls, name):
        userprof = Profile.objects.filter(user__username__icontains = name)
        return userprof



class Image(models.Model):
    image =models.ImageField(upload_to='image/')
    image_name=models.CharField(max_length=30)
    image_caption=models.CharField(max_length=100)
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)
    likes=models.CharField(max_length=150)
    comments=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)

    def save_image(self):
        self.save()
        
     @classmethod
    def get_by_id(cls,id):
        image= Image.objects.get(user = id)
        return image

class Comment(models.Model):
    name=models.CharField(max_length=25)
    user=models.ForeignKey(User,null=True)
    image=models.ForeignKey(Image,related_name='comment')

