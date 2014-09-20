from pyplatformerengine.entities import Entity

"""
    The base entity for all character sprites.
"""
class Character(Entity.Entity):
    
    """
        Initializes the Object.
    """
    def __init__(self, actionComponent, animationComponent, physicsComponent):
        Entity.Entity.__init__(self)
        self.actionComponent = actionComponent
        self.animationComponent = animationComponent
        self.physicsComponent = physicsComponent
    
    """
        Updates the Entity's logic
    """
    def update(self):
        self.actionComponent.determineAction(self)
        Entity.Entity.update(self)
        
    """
        Calls the updates to the graphics
    """
    def draw(self):
        print("TODO")