import pygame

from pyplatformerengine.utilities import Color
from pyplatformerengine.entities.CharacterFactory import CharacterFactory
from pyplatformerengine.utilities.ConsoleManager import ConsoleManager
from pyplatformerengine.utilities.Settings import Settings

"""
    Main game class that handles the loop.
"""
class Game:
    
    colors = Color.Color()
    settings = Settings("../../resources/demo/settings.conf")
    """ 
        Initializes the game setup.
    """
    def __init__(self):
        self.screenWidth = int(self.settings.fetchSetting("screenWidth"))
        self.screenHeight = int(self.settings.fetchSetting("screenHeight"))
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        self.clock = pygame.time.Clock()
    
    """ 
        Begins the game.
    """
    def start_game(self, objectFile):
        done = False
        pygame.init()
        
        allSpriteList = pygame.sprite.Group()
        characterFactory = CharacterFactory(objectFile)
        allEntities = characterFactory.buildSpriteObjects()
        consoleManager = ConsoleManager()
        consoleManager.addToMasterEntityList(allEntities)
        consoleManager.setInScopeEntities(allEntities) 
        camera = characterFactory.buildCamera(self.screenWidth, self.screenHeight)
        
        actionComponent = None
        for entity in consoleManager.getInScopeEntities():
            allSpriteList.add(entity)
            if entity._id == characterFactory.controllingEntityId:
                actionComponent = entity.actionComponent
        
        while not done:
            self.screen.fill(self.colors.BLACK)
            
            for entity in consoleManager.getInScopeEntities():
                entity.update()
                if entity._id == characterFactory.controllingEntityId:
                    camera.update(entity)
                entity.draw()
                self.screen.blit(entity.image, camera.apply(entity))
            
            pygame.display.flip()
            self.clock.tick(60)
            done = actionComponent.endGame
        pygame.quit()
        
        
Game().start_game("../../resources/demo/game_objects/gameObjects.json")
