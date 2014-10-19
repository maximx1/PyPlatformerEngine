class JumpComponent:
    
    """
        Initializes the object.
    """
    def __init__(self, _id, desc):
        self._id = _id
        self.desc = desc
    
    """
        Sets up the component.
    """
    def setUp(self, actor, entity):
        actor.jumpVelocity = actor.stateDict["jumpVelocity"]
    
    """
        Updates the entities jumping state.
    """
    def update(self, actor, entity):
        if entity.readyToJump:
            if entity.initiateJump:
                entity.deltaY = -1 * actor.jumpVelocity
                entity.initiateJump = False
                entity.readyToJump = False
        elif entity.terminateJump:
                entity.readyToJump = True
                entity.deltaY = 0
                entity.terminateJump = False