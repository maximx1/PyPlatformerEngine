from pyplatformerengine.entities import Entity

"""
    The base entity for objects that are visible and can be interacted with by the player.
"""
class PropEntity(Entity.Entity):
    """
        Initializes the Object.
    """
    def __init__(self, proximityComponent, ):
        Entity.Entity.__init__(self)
        
    """
        Updates the Entity's logic
    """
    def update(self):
        Entity.Entity.update(self)
        
    """
        Calls the updates to the graphics
    """
    def draw(self):
        print("TODO")