from pyplatformerengine.entities import Entity

"""
    The base entity for visible objects that the character doesn't interact with.
"""
class DecorativeEntity(Entity.Entity):
    """
        Initializes the Object.
    """
    def __init__(self):
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