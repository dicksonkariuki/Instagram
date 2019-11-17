from django.test import TestCase
from .models import Image,Comment,Profile

class ImageTestClass(TestCase):
    def setUp(self):
        self.post = Image(image_name='Music',image_caption='music is a southing sound that moves souls')

    def test_instance(self):
        self.assertTrue(isinstance(self.post,Image))
