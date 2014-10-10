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
        self.applyJump(entity)
        _, collisionOnYDetected = self.updateLocation(entity)
        self.terminateJumping(entity, collisionOnYDetected)
        
    """
        Applies gravity on an entity for 2d platformer world.
    """
    def applyDownGravity(self, entity):
        if entity.deltaY < self.terminalVelocity:
            entity.deltaY += 1
        elif entity.deltaY > self.terminalVelocity:
            entity.deltaY = self.terminalVelocity
    
    """
        Inverses gravity for a jump action.
    """
    def applyJump(self, entity):
        if entity.initiateJump and entity.readyToJump:
            entity.deltaY = -1 * entity.jumpVelocity
            entity.initiateJump = False
            entity.readyToJump = False
    
    """
        Tells the entity that it is no longer in flight from a jump and defaults to it's terminal velocity.
    """
    def terminateJumping(self, entity, verticalCollisionDetected):
        if verticalCollisionDetected:
            entity.readyToJump = True
            entity.deltaY = 0
    
    """
        Updates the logic location of the entity. Returns True for directional collision.
    """
    def updateLocation(self, entity):
        entity.rect.x += entity.deltaX
        collisionOnXDetected = self.collisionDetectionComponent.detectXCollisions(entity)
        entity.rect.y += entity.deltaY
        collisionOnYDetected = self.collisionDetectionComponent.detectYCollisions(entity)
        return collisionOnXDetected, collisionOnYDetected