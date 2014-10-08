from pyplatformerengine.physics.Gravity import Gravity

"""
    A basic physics component for moving a character around.
"""
class PhysicsComponent:
    
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
        self.applyDownGravity(entity)
        self.updateLocation(entity)
        
    """
        Applies gravity on an entity for 2d platformer world.
    """
    def applyDownGravity(self, entity):
        if entity.deltaY < self.terminalVelocity:
            entity.deltaY += 1
        elif entity.deltaY > self.terminalVelocity:
            entity.deltaY = self.terminalVelocity
    
    def applyJump(self):
        if not self.jumping:
            self.change_y = -1 * self.jumpVelocity
            self.jumping = True
    
    """
        Updates the logic location of the entity.
    """
    def updateLocation(self, entity):
        entity.rect.x += entity.deltaX
        self.collisionDetectionComponent.detectXCollisions(entity)
        entity.rect.y += entity.deltaY
        self.collisionDetectionComponent.detectYCollisions(entity)