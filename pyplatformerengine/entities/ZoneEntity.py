from pyplatformerengine.entities import Entity

"""
    The base entity for objects that aren't visible but can be interacted with by the player.
"""
class ZoneEntity(Entity.Entity):
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