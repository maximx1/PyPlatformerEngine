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
        Detects any collisions with the object in the x direction. Returns True if collision detected.
    """
    def detectXCollisions(self, controllingEntity):
        entityListCopy = self.entities[:]
        entityListCopy.remove(controllingEntity)
        block_hit_list = pygame.sprite.spritecollide(controllingEntity, entityListCopy, False)
        collisionDetected = False
        for block in block_hit_list:
            collisionDetected = True
            if controllingEntity.deltaX > 0:
                controllingEntity.rect.right = block.rect.left
            else:
                controllingEntity.rect.left = block.rect.right
        return collisionDetected
    
    """
        Detects any collisions with the object in the y direction. Returns True if collision detected.
    """
    def detectYCollisions(self, controllingEntity):
        entityListCopy = self.entities[:]
        entityListCopy.remove(controllingEntity)
        block_hit_list = pygame.sprite.spritecollide(controllingEntity, entityListCopy, False)
        collisionDetected = False
        for block in block_hit_list:
            collisionDetected = True
            if controllingEntity.deltaY > 0:
                controllingEntity.rect.bottom = block.rect.top
                controllingEntity.deltaY = 0
            else:
                controllingEntity.rect.top = block.rect.bottom
                controllingEntity.deltaY = 0
        return collisionDetected
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
        