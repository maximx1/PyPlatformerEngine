from pyplatformerengine.physics.BasicCollisionDetection import BasicCollisionDetection

"""
     A collision detection decider
"""
class CollisionDetectionFactory:
    _instance  = None
    registeredActors = []

    """
        Turns new into a singleton retriever.
    """
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(CollisionDetectionFactory, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    """
        Registers the new actor into the collision detection.
    """
    def addCollidable(self, newActor):
        self.registeredActors.add(newActor)
        newActor.collisionDetectionComponent = BasicCollisionDetection()
        
    """
        Initializes the collision detection in the actors.
    """
    def activateCollisionDetection(self):
        for actor in self.registeredActors:
            actor.collisionDetectionComponent.registerEntities(actor, self.registeredActors)