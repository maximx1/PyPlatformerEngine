import pygame

"""
    Basic collision detection system.
"""
class BasicCollisionDetection:
    
    """
        Initializes the object.
    """
    def __init__(self):
        self.entities = []
        
    """
        Detects any collisions in the object.
    """
    def detectXCollisions(self, controllingEntity):
        block_hit_list = pygame.sprite.spritecollide(controllingEntity, self.entities[1:], False)
        for block in block_hit_list:
            if controllingEntity.deltaX > 0:
                controllingEntity.rect.right = block.rect.left
            else:
                controllingEntity.rect.left = block.rect.right
    
    def detectYCollisions(self, controllingEntity):
        block_hit_list = pygame.sprite.spritecollide(controllingEntity, self.entities[1:], False)
        for block in block_hit_list:
            if controllingEntity.deltaY > 0:
                controllingEntity.rect.bottom = block.rect.top
                controllingEntity.deltaY = 0
            else:
                controllingEntity.rect.top = block.rect.bottom
                controllingEntity.deltaY = 0
    """
        Registers an entity with the collision detection system. 
    """    
    def registerEntity(self, entity):
        self.entities.append(entity)
        
    """
        Registers all entities to the system.
    """
    def registerEntities(self, entities):
        self.entities = entities
        