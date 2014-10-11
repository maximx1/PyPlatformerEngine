from pygame import Rect

"""
    Utility to help create a camera.
"""
class CameraMan:
    
    """
        Initializes the object.
    """
    def __init__(self, screenWidth, screenHeight):
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.halfWidth = int(screenWidth / 2)
        self.halfHeight = int(screenHeight / 2)
    
    """
        Builds a complex camera
    """
    def complexCamera(self, camera, target_rect):
        l, t, _, _ = target_rect
        _, _, w, h = camera
        l, t, _, _ = -l + self.halfWidth, -t + self.halfHeight, w, h
    
        l = min(0, l)                           # stop scrolling at the left edge
        l = max(-(camera.width - self.screenWidth), l)   # stop scrolling at the right edge
        t = max(-(camera.height - self.screenHeight), t) # stop scrolling at the bottom
        t = min(0, t)                           # stop scrolling at the top
        return Rect(l, t, w, h)