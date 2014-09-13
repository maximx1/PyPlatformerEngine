from pyplatformerengine.entities import Character

"""
    Entity for an on screen controllable character.
"""
class NonPlayableCharacter(Character.Character):
    
    """
        Initializes the Object.
    """
    def __init__(self):
        Character.Character.__init__(self)
        
    """
        Updates the Entity's logic
    """
    def update(self):
        Character.Character.update(self)