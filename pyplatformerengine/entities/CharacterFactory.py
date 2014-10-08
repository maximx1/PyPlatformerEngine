from pyplatformerengine.entities.Character import Character
from pyplatformerengine.physics.BasicCollisionDetection import BasicCollisionDetection
from pyplatformerengine.utilities.CameraMan import CameraMan
from pyplatformerengine.entities.Camera import Camera
from pyplatformerengine.entities.SpritesheetFactory import SpritesheetFactory
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
        Builds a camera with the level details.
    """
    def buildCamera(self, screenWidth, screenHeight):
        objectData = self.parseFile()
        level = objectData["level"]
        cameraMan = CameraMan(screenWidth, screenHeight)
        return Camera(cameraMan, level["width"], level["height"])

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
        spritesheetFactory = SpritesheetFactory()
        image = spritesheetFactory.createImage(obj)
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
        entity.maximumLeftRightVelocity = obj.get("leftRightMaxVelocity", 1)
        # TODO: add proximity
        return entity
    
    """
        Utility to get a class by name and module.
    """
    def importClass(self, moduleName, className):
        mod = __import__(str(moduleName), fromlist=[str(className)])
        return getattr(mod, str(className))