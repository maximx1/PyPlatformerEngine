from pyplatformerengine.entities import *

class CharacterFactory:
    def __init__(self, objectFile):
        self.objectFile = objectFile

    def parseFile(self):
        print("Hello")
        
    def my_import(self, name):
        mod = __import__(name)
        components = name.split('.')
        for comp in components[1:]:
            mod = getattr(mod, comp)
        return mod