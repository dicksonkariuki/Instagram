from django.test import TestCase
from .models import Image,Comment,Profile

class ImageTestClass(TestCase):
    def setUp(self):
        self.post = Image(image_name='Farming',image_caption='Farming is the backbone of our economy')

    def test_instance(self):
        self.assertTrue(isinstance(self.post,Image))

    def test_save_image(self):
        self.post.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)
class CommentTestClass(TestCase):
    def setUp(self):
        self.post=Comment(name='nice')