from pyplatformerengine.entities.Character import Character
from pyplatformerengine.utilities.Color import Color
from pyplatformerengine.physics.BasicCollisionDetection import BasicCollisionDetection
import pygame
import json

"""
    Entity builder compatible with "v1" of JSON "scriptVersion"
"""
class CharacterFactory:
    
    controllingEntityId = 1
    
    """
        Initializes the object with an object file.
    """
    def __init__(self, objectFile):
        self.objectFile = objectFile
        
    """
        Loads and builds game entities.
    """
    def buildSpriteObjects(self):
        objectData = self.parseFile()
        gameEntities = []
        collisionEntities = []
        for obj in objectData["gameObjects"]:
            newGameEntity = self.createObject(obj)
            gameEntities.append(newGameEntity)
            if newGameEntity.collisionEnabled:
                collisionEntities.append(newGameEntity)
        self.determineControllingEntity(objectData["gameObjects"])
        for entity in gameEntities:
            if entity.collisionEnabled:
                entity.physicsComponent.collisionDetectionComponent.registerEntities(collisionEntities)
        return gameEntities

    """
        Determines the controlling entity from the config. Chooses the first entity.
    """
    def determineControllingEntity(self, gameObjects):
        for obj in gameObjects:
            if obj.get("controllingEntity", 0) == 1:
                self.controllingEntityId = obj["_id"]

    """
        Parses a game file.
    """
    def parseFile(self):
        objectDataStream = open(self.objectFile)
        objectData = json.load(objectDataStream)
        objectDataStream.close()
        return objectData
    
    """
        Creates a game object based on config.
    """
    def createObject(self, obj):
        image = self.createImage(obj)
        startX = int(obj["startPositionX"])
        startY = int(obj["startPositionY"])
        collisionDetectionComponent = BasicCollisionDetection()
        actionComponent = self.importClass(obj["actionCompMod"], obj["actionCompClass"])()
        animationComponent = self.importClass(obj["animationCompMod"], obj["animationCompClass"])()
        physicsComponent = self.importClass(obj["physicsCompMod"], obj["physicsCompClass"])(obj["terminalVelocity"], collisionDetectionComponent)
        entity = Character(actionComponent, animationComponent, physicsComponent, image, startX, startY)
        entity._id = obj["_id"]
        entity.name = obj["name"]
        entity.collisionEnabled = False if obj["collisionEnabled"] == 0 else True
        # TODO: add proximity
        return entity
        
    """
        Creates a visual game object based on configuration.
    """
    def createImage(self, obj):
        color = self.choosePredefinedColor(obj["spritesheetFill"])
        
        if obj["spriteImgType"] == "PYGAME_SURFACE":
            return self.createGenericSurface(obj["spritesheetX"], obj["spritesheetY"], color)
    
    """
        Convert color string to actual color.
    """
    def choosePredefinedColor(self, colorName):
        color = Color.BLACK
        if colorName == "WHITE":
            color = Color.WHITE
        elif colorName == "RED":
            color = Color.RED
        elif colorName == "PINK":
            color = Color.PINK
        elif colorName == "BLUE":
            color = Color.BLUE
        elif colorName == "GREEN":
            color = Color.GREEN
        return color
    
    """
        Creates a generic pygame surface.
    """
    def createGenericSurface(self, width, height, color):
        image = pygame.Surface([width, height])
        image.fill(color)
        return image
        
    """
        Utility to get a class by name and module.
    """
    def importClass(self, moduleName, className):
        mod = __import__(str(moduleName), fromlist=[str(className)])
        return getattr(mod, str(className))