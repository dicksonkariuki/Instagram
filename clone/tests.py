from django.test import TestCase
from .models import Image,Comment,Profile

class ImageTestClass(TestCase):
    def setUp(self):
        self.post = Image(image_name='Farming',image_caption='Farming is the backbone of our economy')

    def test_instance(self):
        self.assertTrue(isinstance(self.post,Image))

    # def test_save_image(self):
    #     self.post.save_image()
    #     images = Image.objects.all()
    #     self.assertTrue(len(images)>0)
class CommentTestClass(TestCase):
    def setUp(self):
        self.post=Comment(name='nice')
    def test_instance(self):
        self.assertTrue(isinstance(self.post,Comment))
    def test_save_comment(self):
        self.post.save_comment()
        comments=Comment.objects.all()
        self.assertTrue(len(comments)>0)
class ProfileTestClass(TestCase):
    def setUp(self):
        self.post=Profile(bio='I am a software engineer')
    def test_instance(self):
        self.assertTrue(isinstance(self.post,Profile))
    
    def test_save_profile(self):
        self.post.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)>0)