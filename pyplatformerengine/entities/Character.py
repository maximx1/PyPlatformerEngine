from pyplatformerengine.entities import Entity
import pygame

"""
    The base entity for all character sprites.
"""
class Character(Entity.Entity):
    
    deltaX = 0
    deltaY = 0
    direction = 1
    isJumping = False
    
    """
        Initializes the Object.
    """
    def __init__(self, actionComponent, animationComponent, physicsComponent):
        Entity.Entity.__init__(self)
        self.actionComponent = actionComponent
        self.animationComponent = animationComponent
        self.physicsComponent = physicsComponent
        self.rect = pygame.Rect(10, 0, 100, 100)
    
    """
        Updates the Entity's logic
    """
    def update(self):
        self.actionComponent.determineAction(self)
        self.physicsComponent.update(self)
        Entity.Entity.update(self)
        
    """
        Calls the updates to the graphics
    """
    def draw(self):
        self.animationComponent.draw(self)