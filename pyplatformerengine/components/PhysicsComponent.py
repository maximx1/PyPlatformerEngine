from pyplatformerengine.physics.Gravity import Gravity

class PhysicsComponent:
    
    terminalVelocity = 0
    
    """
        Initializes the object.
    """
    def __init__(self, terminalVelocity):
        self.terminalVelocity = terminalVelocity
    
    """
        Runs the update to the logic component.
    """
    def update(self, entity):
        self.applyDownGravity(entity)
        
    """
        Applies gravity on an entity for 2d platformer world.
    """
    def applyDownGravity(self, entity):
        if entity.deltaY < self.terminalVelocity:
            entity.deltaY += 1
        elif entity.deltaY > self.terminalVelocity:
            entity.deltaY = self.terminalVelocity