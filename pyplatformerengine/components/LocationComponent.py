from pyplatformerengine.physics.Gravity import Gravity
from pyplatformerengine.physics.CollisionDetectionFactory import CollisionDetectionFactory
from pygame.rect import Rect

"""
    A basic physics component for moving a character around.
"""
class LocationComponent:
    
    """
        Initializes the object.
    """
    def __init__(self, _id, desc):
        self._id = _id
        self.desc = desc
    
    """
        Sets up the object.
    """
    def setUp(self, actor, entity):
        entity.rect = Rect(actor.stateDict["startPositionX"], actor.stateDict["startPositionY"], 1, 1)
        if actor.stateDict["collisionEnabled"] != 0:
            collisionDetectionFactory = CollisionDetectionFactory()
            collisionDetectionFactory.addCollidable(actor, entity)
        
    """
        Updates the logic location of the entity. Returns True for directional collision.
    """
    def update(self, actor, entity):
        entity.rect.x += entity.deltaX
        actor.collisionDetectionComponent.detectXCollisions(entity)
        entity.rect.y += entity.deltaY
        collisionOnYDetected = actor.collisionDetectionComponent.detectYCollisions(entity)
        if collisionOnYDetected:
            entity.terminateJump = True