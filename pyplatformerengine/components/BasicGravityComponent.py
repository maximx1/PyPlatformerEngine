class BasicGravityComponent:
    
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
        actor.terminalVelocity = actor.stateDict["terminalVelocity"]
        
    """
        Applies gravity on an entity for 2d platformer world.
    """
    def update(self, actor, entity):
        if entity.deltaY < self.terminalVelocity:
            entity.deltaY += 1
        elif entity.deltaY > self.terminalVelocity:
            entity.deltaY = self.terminalVelocity