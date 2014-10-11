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
    def __init__(self, actionComponent, animationComponent, physicsComponent, spriteStages, startX, startY):
        pygame.sprite.Sprite.__init__(self)
        self.actionComponent = actionComponent
        self.animationComponent = animationComponent
        self.physicsComponent = physicsComponent
        self.spriteStages = spriteStages
        self.animationComponent.initializeCharacter(self, startX, startY)
    
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