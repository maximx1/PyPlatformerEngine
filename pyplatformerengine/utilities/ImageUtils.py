import pygame

"""
    Some image utilities for sprites.
"""
class ImageUtils:
    
    """
        Scales an image.
    """
    def scaleImage(self, image, newWidth, newHeight) :
        return pygame.transform.scale(image, (newWidth, newHeight))