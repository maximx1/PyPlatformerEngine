import pygame

"""
    Settings manager  
"""
class Settings:
    
    """ 
        Initializes the object
    """
    def __init__(self,path):
        self.settings = {}
        settingsFile = open(path, "r")
        for line in settingsFile:
            settingName,settingValue = line.split("=")
            self.settings[settingName] = settingValue.rstrip('\n')

    def changeSetting(self,settingName,change):
        if self.settings.get(settingName):
            self.settings[settingName] = change
    
    def fetchSetting(self,settingName):
        if self.settings.get(settingName):
            return self.settings[settingName]
        else:
            return "-1"
