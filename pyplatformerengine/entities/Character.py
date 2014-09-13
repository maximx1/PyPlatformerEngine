from pyplatformerengine.entities import DynamicEntity

"""
    The base entity for all character sprites.
"""
class Character(DynamicEntity.DynamicEntity):
    
    """
        Initializes the Object.
    """
    def __init__(self):
        DynamicEntity.DynamicEntity.__init__(self)
    
    """
        Updates the Entity's logic
    """
    def update(self):
        DynamicEntity.DynamicEntity.update(self)