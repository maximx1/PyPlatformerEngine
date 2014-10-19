import unittest
import pygame
from pyplatformerengine.utilities.ImageUtils import ImageUtils

class TestImageUtils(unittest.TestCase):
    def setUp(self):
        self.testImage = pygame.image.load("test/utilities/BasicBall.png")
        self.image = ImageUtils(self.testImage)
                
    def testImageMethodsForManipulatingImages(self):
        self.assertEqual(self.testImage, self.image.getImage(), "Images are not the same")
        self.assertNotEqual(self.image.getImage(), self.image.scale(2,2).getImage(), "Images are the same (scale)")
        self.assertNotEqual(self.image.getImage(), self.image.rotate(20).getImage(), "Images are the same (rotate)")
        self.assertNotEqual(self.image.getImage(), self.image.flipVertical().getImage(), "Images are the same (flipVertical)")
        self.assertNotEqual(self.image.getImage(), self.image.flipHorizontal().getImage(), "Images are the same (flipHorizontal)")
