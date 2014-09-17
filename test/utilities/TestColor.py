import unittest
from pyplatformerengine.utilities.Color import Color

class TestColor(unittest.TestCase):
    def setUp(self):
        self.color = Color()
        
    def testColorClassIsBuiltWithAllBaseColors(self):
        self.assertEqual((0, 0, 0), self.color.BLACK, "BLACK is invalid")
        self.assertEqual((255, 20, 147), self.color.PINK, "PINK is invalid")
        self.assertEqual((255, 255, 255), self.color.WHITE, "WHITE is invalid")
        self.assertEqual((255, 0, 0), self.color.RED, "RED is invalid")
        self.assertEqual((0, 255, 0), self.color.GREEN, "GREEN is invalid")
        self.assertEqual((0, 0, 255), self.color.BLUE, "BLUE is invalid")