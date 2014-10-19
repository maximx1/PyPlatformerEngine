import pygame

"""
    The base entity for all character sprites.
"""
class Entity(pygame.sprite.Sprite):
    
    deltaX = 0
    deltaY = 0
    direction = 1
    initiateJump = False
    readyToJump = False
    
    """
        Initializes the Object.
    """
    def __init__(self, updateActors, drawActors):
        pygame.sprite.Sprite.__init__(self)
        self.updateActors = updateActors
        self.drawActors = drawActors
    
    """
        Updates the Entity's logic
    """
    def update(self):
        for actor in self.updateActors:
            actor.act()
        
    """
        Calls the updates to the graphics
    """
    def draw(self):
        for actor in self.drawActors:
            actor.act()