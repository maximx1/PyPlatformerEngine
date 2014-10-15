import unittest
from pyplatformerengine.utilities.Settings import Settings

class TestSettings(unittest.TestCase):
    def setUp(self):
        self.settings = Settings("test/utilities/settings.conf")
        
    def testFetchSettingReturnsValue(self):
        self.assertEqual("800", self.settings.fetchSetting("screenWidth"), "screenWidth does not equal 800")
        self.assertEqual("600", self.settings.fetchSetting("screenHeight"), "screenHeight does not equal 600")
        self.assertEqual("True", self.settings.fetchSetting("debug"), "debug does not equal True")
        self.settings.changeSetting("screenWidth","1280")
        self.settings.changeSetting("screenHeight","720")
        self.settings.changeSetting("debug","False")
        self.assertEqual("1280", self.settings.fetchSetting("screenWidth"), "screenWidth does not equal 1280")
        self.assertEqual("720", self.settings.fetchSetting("screenHeight"), "screenHeight does not equal 720")
        self.assertEqual("False", self.settings.fetchSetting("debug"), "debug does not equal False")
