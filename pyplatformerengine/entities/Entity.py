import pygame

"""
    The base entity for all character sprites.
"""
class Entity(pygame.sprite.Sprite):
    
    deltaX = 0
    deltaY = 0
    direction = 1
    initiateJump = False
    terminateJump = False
    readyToJump = False
    
    """
        Initializes the Object.
    """
    def __init__(self, _id, updateActors, drawActors):
        pygame.sprite.Sprite.__init__(self)
        self._id = _id
        self.updateActors = updateActors
        self.drawActors = drawActors
        
    """
        Sets up all of the actors if their components need setup.
    """
    def activateActors(self):
        for actor in self.updateActors:
            actor.setUp(self)
        for actor in self.drawActors:
            actor.setUp(self)
    
    """
        Updates the Entity's logic
    """
    def update(self):
        for actor in self.updateActors:
            actor.act(self)
        
    """
        Calls the updates to the graphics
    """
    def draw(self):
        for actor in self.drawActors:
            actor.act(self)