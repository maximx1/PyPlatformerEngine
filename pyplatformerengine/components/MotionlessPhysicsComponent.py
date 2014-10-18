from pygame.rect import Rect

"""
    A basic physics component for moving a character around.
"""
from pyplatformerengine.physics.CollisionDetectionFactory import CollisionDetectionFactory
class MotionlessPhysicsComponent:
    
    """
        Sets up the object.
    """
    def setUp(self, actor, entity):
        entity.rect = Rect(actor.stateDict["startPositionX"], actor.stateDict["startPositionY"], 1, 1)
        if actor.stateDict["collisionEnabled"] != 0:
            collisionDetectionFactory = CollisionDetectionFactory()
            collisionDetectionFactory.addCollidable(actor)
    
    """
        Runs the update to the logic component.
    """
    def update(self, actor, entity):
        self.updateLocation(entity)
    
    """
        Updates the logic location of the entity.
    """
    def updateLocation(self, entity):
        entity.rect.x += entity.deltaX
        entity.rect.y += entity.deltaY