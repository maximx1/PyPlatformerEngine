from pyplatformerengine.entities import Entity

"""
    The base entity for objects that don't move relative to their coordinates in the map.
"""
class StaticEntity(Entity.Entity):
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