import pygame

from pyplatformerengine.utilities import Color
from pyplatformerengine.entities.CharacterFactory import CharacterFactory
from pyplatformerengine.utilities.ConsoleManager import ConsoleManager
from pyplatformerengine.utilities.LoggerUtil import LoggerUtil
from pyplatformerengine.utilities.Settings import Settings
from pyplatformerengine.physics.CollisionDetectionFactory import CollisionDetectionFactory

"""
    Main game class that handles the loop.
"""
class Game:
    
    colors = Color.Color()
    """ 
        Initializes the game setup.
    """
    def __init__(self, settingsFile):
        settings = Settings(settingsFile).settings
        settings["enableLogging"] = True if settings["enableLogging"] == "True" else False
        self.screenWidth = int(settings["screenWidth"])
        self.screenHeight = int(settings["screenHeight"])
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        self.clock = pygame.time.Clock()
        loggerUtil = LoggerUtil()
        loggerUtil.setLogger(settings)
    
    """ 
        Begins the game.
    """
    def start_game(self, objectFile):
        done = False
        pygame.init()
        
        allSpriteList = pygame.sprite.Group()
        characterFactory = CharacterFactory(objectFile)
        allEntities = characterFactory.createGameObjects()
        consoleManager = ConsoleManager()
        consoleManager.addToMasterEntityList(allEntities)
        consoleManager.setInScopeEntities(allEntities) 
        camera = characterFactory.buildCamera(self.screenWidth, self.screenHeight)
        
        controllingActor = consoleManager.controllingActor
        for entity in consoleManager.getInScopeEntities():
            allSpriteList.add(entity)
            
        CollisionDetectionFactory().activateCollisionDetection()
        
        while not done:
            self.screen.fill(self.colors.BLACK)
            
            for entity in sorted(consoleManager.getInScopeEntities(), key=lambda x: x._id):
                entity.update()
                if entity._id == consoleManager.cameraFocusEntityId:
                    camera.update(entity)
                entity.draw()
                self.screen.blit(entity.image, camera.apply(entity))
            
            pygame.display.flip()
            self.clock.tick(60)
            done = controllingActor.endGame
        pygame.quit()
        
        
Game("../../resources/demo/settings.conf").start_game("../../resources/demo/game_objects/gameObjects.json")
