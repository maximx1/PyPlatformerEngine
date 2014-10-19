from pyplatformerengine.entities.Entity import Entity
from pyplatformerengine.physics.BasicCollisionDetection import BasicCollisionDetection
from pyplatformerengine.utilities.CameraMan import CameraMan
from pyplatformerengine.entities.Camera import Camera
from pyplatformerengine.entities.SpritesheetFactory import SpritesheetFactory
from pyplatformerengine.actors.ActorFactory import ActorFactory
import pygame
import json

"""
    Entity builder compatible with "v1" of JSON "scriptVersion"
"""
class CharacterFactory:
    
    """
        Initializes the object with an object file.
    """
    def __init__(self, objectFile):
        self.objectFile = objectFile
        self.objectData = self.parseFile()

    """
        Builds a camera with the level details.
    """
    def buildCamera(self, screenWidth, screenHeight):
        level = self.objectData["level"]
        cameraMan = CameraMan(screenWidth, screenHeight)
        return Camera(cameraMan, level["width"], level["height"])

    """
        Parses a game file.
    """
    def parseFile(self):
        objectDataStream = open(self.objectFile)
        objectData = json.load(objectDataStream)
        objectDataStream.close()
        return objectData
    
    """
        Creates the in game objects
    """
    def createGameObjects(self):
        gameEntities = []
        actorFactory = ActorFactory()
        components = actorFactory.buildComponents(self.objectData["components"])

        for obj in self.objectData["gameObjects"]:
            newGameEntity = self.createGameObject(obj, components, actorFactory)
            gameEntities.append(newGameEntity)
            
        return gameEntities
    
    """
        Creates an in game object.
    """
    def createGameObject(self, obj, components, actorFactory):
        updateActors, drawActors = actorFactory.buildActors(obj["actors"], components)
        return Entity(updateActors, drawActors)
