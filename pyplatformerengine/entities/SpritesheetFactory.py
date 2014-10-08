from pyplatformerengine.utilities.Color import Color
from pyplatformerengine.models.SpritesheetLoader import SpritesheetLoader
from pyplatformerengine.utilities.ImageUtils import ImageUtils

import pygame

"""
    Class utility to build sprites.
"""
class SpritesheetFactory:
    
    """
        Creates a visual game object based on configuration.
    """
    def createImage(self, obj):
        color = self.choosePredefinedColor(obj["spritesheetFill"])
        
        if obj["spriteImgType"] == "PYGAME_SURFACE":
            return self.createGenericSurface(obj["spritesheetX"], obj["spritesheetY"], color)
        elif obj["spriteImgType"] == "SPRITE_NO_ANIMATION":
            return self.loadNonAnimatedSprite(obj, Color.BLACK)
        
    """
        Convert color string to actual color.
    """
    def choosePredefinedColor(self, colorName):
        color = Color.BLACK
        if colorName == "WHITE":
            color = Color.WHITE
        elif colorName == "RED":
            color = Color.RED
        elif colorName == "PINK":
            color = Color.PINK
        elif colorName == "BLUE":
            color = Color.BLUE
        elif colorName == "GREEN":
            color = Color.GREEN
        return color
    
    """
        Creates a generic pygame surface.
    """
    def createGenericSurface(self, width, height, color):
        image = pygame.Surface([width, height])
        image.fill(color)
        return image
    
    """
        Creates a non animated sprite.
    """
    def loadNonAnimatedSprite(self, obj, color):
        spritesheetLoader = SpritesheetLoader()
        spriteMap = spritesheetLoader.loadSpriteMap(obj["spritesheetImg"])
        image = spritesheetLoader.imageAt(spriteMap, (0, 0, obj["spritesheetImgSizeX"],obj["spritesheetImgSizeY"]), color)
        imageUtils = ImageUtils()
        return imageUtils.scaleImage(image, obj["spritesheetX"], obj["spritesheetY"])