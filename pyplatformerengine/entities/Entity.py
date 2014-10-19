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
        self.actionComponent.determineAction(self)
        self.physicsComponent.update(self)
        
    """
        Calls the updates to the graphics
    """
    def draw(self):
        self.animationComponent.draw(self)