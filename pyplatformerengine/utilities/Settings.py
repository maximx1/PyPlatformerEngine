"""
    Settings manager  
"""
class Settings:
    
    """ 
        Initializes the object by passing in path for the settings file.
        For settings such as pathname for log files may be quoted, this 
        filters for quotes(single and double) 
    """
    def __init__(self,path):
        self.settings = {}
        settingsFile = open(path, "r")
        for line in settingsFile:
            settingName,settingValue = line.split("=")
            settingValue = settingValue.replace('"','')
            settingValue = settingValue.replace("'","")
            self.settings[settingName] = settingValue.rstrip('\n')

    def changeSetting(self,settingName,change):
        if self.settings.get(settingName):
            self.settings[settingName] = change
    
    def fetchSetting(self,settingName):
        if self.settings.get(settingName):
            return self.settings[settingName]