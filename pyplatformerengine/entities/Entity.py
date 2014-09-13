import pygame

"""
    Base for all entities in the engine.
"""
class Entity(pygame.sprite.Sprite):
    """
        Initializes the Object.
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
       
    """
        Calls the common core update features.
    """ 
    def update(self):
        print("TODO")