import unittest
import pygame
from pyplatformerengine.utilities.ImageUtils import ImageUtils

class TestImageUtils(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.testImage = pygame.image.load("./BasicBall.png")
        self.image = ImageUtils(self.testImage)
                
    def testImageMethodsForManipulatingImages(self):
        self.assertEqual(self.image.getImage, self.image.getImage, "Images are not the same")
        self.assertNotEqual(self.image.getImage, self.image.scale(2,2), "Images are the same (scale)")
        self.assertNotEqual(self.image.getImage, self.image.rotate(20), "Images are the same (rotate)")
        self.assertNotEqual(self.image.getImage, self.image.flipVertical, "Images are the same (flipVertical)")
        self.assertNotEqual(self.image.getImage, self.image.flipHorizontal, "Images are the same (flipHorizontal)")
