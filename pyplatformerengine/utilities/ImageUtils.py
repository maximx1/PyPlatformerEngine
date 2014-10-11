import pygame

"""
    Some image utilities for sprites.
"""
class ImageUtils:
    
    """
        Initializes the object
    """
    def __init__(self, image):
        self.image = image
    
    """
        Scales an image.
    """
    def scale(self, newWidth, newHeight) :
        self.image = pygame.transform.scale(self.image, (newWidth, newHeight))
        return self
        
    """
        rotates an image.
    """
    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.image, angle)
        return self
    
    """
        Flips a sprite over its x-axis
    """
    def flipVertical(self):
        self.image = pygame.transform.flip(self.image, False, True)
        return self
    
    """
        Flips a sprite over its y-axis
    """
    def flipHorizontal(self):
        self.image = pygame.transform.flip(self.image, True, False)
        return self
        
    """
        Gets the final image
    """
    def getImage(self):
        return self.image