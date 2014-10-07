from pygame import *

class Camera(object):
    def __init__(self, cameraMan, width, height):
        self.cameraMan = cameraMan
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.cameraMan.complexCamera(self.state, target.rect)