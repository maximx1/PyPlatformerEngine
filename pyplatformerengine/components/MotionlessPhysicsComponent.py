from pyplatformerengine.physics.Gravity import Gravity

"""
    A basic physics component for moving a character around.
"""
class MotionlessPhysicsComponent:
    
    """
        Initializes the object.
    """
    def __init__(self, terminalVelocity, collisionDetectionComponent):
        self.terminalVelocity = terminalVelocity
        self.collisionDetectionComponent = collisionDetectionComponent
    
    """
        Runs the update to the logic component.
    """
    def update(self, entity):
        self.updateLocation(entity)
    
    """
        Updates the logic location of the entity.
    """
    def updateLocation(self, entity):
        entity.rect.x += entity.deltaX
        entity.rect.y += entity.deltaY