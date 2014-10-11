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
    def createImages(self, obj):
        color = self.choosePredefinedColor(obj["spritesheetFill"])
        
        spriteStages = {}
        for img in obj["spriteSheetImages"]:
            if img["type"] == "PYGAME_SURFACE":
                spriteStages[img["label"]] = self.createGenericSurface(img, color)
            elif img["type"] == "SPRITE_IMG":
                spriteStages[img["label"]] = self.loadSpriteAnimations(img, Color.BLACK)
        return spriteStages
        
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
    def createGenericSurface(self, img, color):
        image = pygame.Surface((img["width"], img["height"]))
        image.fill(color)
        return image
    
    """
        Loads the sprites from the spritemap.
    """
    def loadSpriteAnimations(self, img, color):
        spritesheetLoader = SpritesheetLoader()
        spriteMap = spritesheetLoader.loadSpriteMap(img["file"])
        image = spritesheetLoader.imageAt(spriteMap, (img["x"], img["y"], img["width"], img["height"]), color)
        return image
            