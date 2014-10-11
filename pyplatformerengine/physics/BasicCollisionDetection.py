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
        block_hit_list = pygame.sprite.spritecollide(controllingEntity, self.entities, False)
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
        block_hit_list = pygame.sprite.spritecollide(controllingEntity, self.entities, False)
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
    def registerEntity(self, controllingEntity, entity):
        self.entities.append(entity)
        entityListCopy = self.entities[:]
        entityListCopy.remove(controllingEntity)
        self.entities = entityListCopy
        
    """
        Registers all entities to the system.
    """
    def registerEntities(self, controllingEntity, entities):
        entityListCopy = entities[:]
        entityListCopy.remove(controllingEntity)
        self.entities = entityListCopy
        