import unittest
import pygame
from pyplatformerengine.utilities.ProximityManager import ProximityManager

class TestProximityManager(unittest.TestCase):
    def setUp(self):
        self.entityRect = pygame.Rect(0,0,100,100)
        # TODO: Gotta fix this shtuff
    
    def testCanCalculateObjectRadiusAndCenterpoint(self):
        class Tmp:
            iHeight = 100
            iWidth = 100
        entity = Tmp()
        entity.rect = self.entityRect
        proximityManager = ProximityManager(None)
        radius, x, y = proximityManager.calculateObjectRadiusAndCenterpoint(entity)
        self.assertEqual(70, radius, "Should be the radius of the entity.")
        self.assertEqual(50, x, "Should be half of the original")
        self.assertEqual(50, y, "Should be half of the original")
        
    def testCanReturnTrueIfObjectIsInProximity(self):
        proximityManager = ProximityManager(None)
        result = proximityManager.determineIfObjectsAreInVicinity(5, 5, 30, 20, 20, 10)
        self.assertTrue(result)
    
    def testCanReturnFalseIfObjectIsInProximity(self):
        proximityManager = ProximityManager(None)
        result = proximityManager.determineIfObjectsAreInVicinity(5, 5, 30, 70, 70, 10)
        self.assertFalse(result)
        