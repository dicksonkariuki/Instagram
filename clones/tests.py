from django.test import TestCase
from .models import Image,Comment,Profile

class ImageTestClass(TestCase):
    def setUp(self):
        self.image_name = Image(image_name='Farming',image_caption='Farming is the backbone of our economy')

    def test_instance(self):
        self.assertTrue(isinstance(self.image_name,Image))

    def test_save_image(self):
        self.image_caption.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)
class CommentTestClass(TestCase):
    def setUp(self):
        self.comment=Comment(comment='nice')
    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comment))
    def test_save_comment(self):
        self.post.save_comment()
        comments=Comment.objects.all()
        self.assertTrue(len(comments)>0)
class ProfileTestClass(TestCase):
    def setUp(self):
        self.bio=Profile(bio='I am a software engineer')
    def test_instance(self):
        self.assertTrue(isinstance(self.bio,Profile))
    
    def test_delete_profile(self):
        self.bio.delete_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)>0)