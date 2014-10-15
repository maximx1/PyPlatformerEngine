import unittest
from pygame.rect import Rect
from pyplatformerengine.utilities.CameraMan import CameraMan

class TestCameraMan(unittest.TestCase):
    def testCamaraManPopulatesAttributes(self):
        cameraMan = CameraMan(100, 100)
        self.assertEqual(100, cameraMan.screenHeight, "Screen height should be what was passed in.")
        self.assertEqual(100, cameraMan.screenWidth, "Screen width should be what was passed in.")
        self.assertEqual(50, cameraMan.halfHeight, "Half height should be half of what was passed in.")
        self.assertEqual(50, cameraMan.halfHeight, "Half width should be half of what was passed in.")
        
    def testCanStopAtLeftEdge(self):
        entityRect = Rect(-5,0,100,100)
        cameraRect = Rect(0,0,1600, 600)
        cameraMan = CameraMan(800, 600)
        l, _, _, _ = cameraMan.complexCamera(cameraRect, entityRect)
        self.assertEqual(0, l, "Should have stopped at the left edge of the screen")
        
    
    def testCanStopAtRightEdge(self):
        entityRect = Rect(1700,0,100,100)
        cameraRect = Rect(0,0,1600, 600)
        cameraMan = CameraMan(800, 600)
        l, _, _, _ = cameraMan.complexCamera(cameraRect, entityRect)
        self.assertEqual(-800, l, "Should have stopped at the right edge of the screen")
        
    
    def testCanStopAtTopEdge(self):
        entityRect = Rect(0,-5,100,100)
        cameraRect = Rect(0,0,1600, 600)
        cameraMan = CameraMan(800, 600)
        _, t, _, _ = cameraMan.complexCamera(cameraRect, entityRect)
        self.assertEqual(0, t, "Should have stopped at the top edge of the screen")
        
    
    def testCanStopAtBottomEdge(self):
        entityRect = Rect(0,700,100,100)
        cameraRect = Rect(0,0,1600, 600)
        cameraMan = CameraMan(800, 600)
        _, t, _, _ = cameraMan.complexCamera(cameraRect, entityRect)
        self.assertEqual(0, t, "Should have stopped at the bottom edge of the screen")