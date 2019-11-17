from django.db import models

class Profile(models.Model):
    profile_photo =models.ImageField(upload_to ='profile/')
    bio =models.CharField(max_length=50)



class Image(models.Model):
    image =models.ImageField(upload_to='image/')
    image_name=models.CharField(max_length=30)
    image_caption=models.CharField(max_length=100)
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)
    likes=models.CharField(max_length=150)
    comments=models.CharField(max_length=100)

    def save_image(self):
        self.save()

class Comment(models.Model):
    name=models.CharField(max_length=25)
    user=models.ForeignKey(User,null=True)
    image=models.ForeignKey(image,related_name='comment')

