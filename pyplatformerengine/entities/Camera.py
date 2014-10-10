from pygame.rect import Rect

"""
    The camera class that calls character blitting.
"""
class Camera(object):
    
    """
        Initializes the object.
    """
    def __init__(self, cameraMan, width, height):
        self.cameraMan = cameraMan
        self.state = Rect(0, 0, width, height)

    """
        Applies the update from the camera.
    """
    def apply(self, target):
        return target.rect.move(self.state.topleft)

    """
        Updates the state of the blit.
    """
    def update(self, target):
        self.state = self.cameraMan.complexCamera(self.state, target.rect)