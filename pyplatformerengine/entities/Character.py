from pyplatformerengine.entities import Entity
from pyplatformerengine.utilities.Color import Color

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
    def __init__(self, actionComponent, animationComponent, physicsComponent, img, startX, startY):
        Entity.Entity.__init__(self)
        self.actionComponent = actionComponent
        self.animationComponent = animationComponent
        self.physicsComponent = physicsComponent
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = startX
        self.rect.y = startY
    
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