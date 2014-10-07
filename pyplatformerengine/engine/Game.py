import pygame

from pyplatformerengine.utilities import Color
from pyplatformerengine.entities.CharacterFactory import CharacterFactory

"""
    Main game class that handles the loop.
"""
class Game:
    
    colors = Color.Color()
    
    """
        Initializes the game setup.
    """
    def __init__(self):
        self.screenWidth = 800
        self.screenHeight = 600
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        self.clock = pygame.time.Clock()
        
    """
        Begins the game.
    """
    def start_game(self):
        done = False
        pygame.init()
        
        allSpriteList = pygame.sprite.Group()
        characterFactory = CharacterFactory("../../resources/demo/game_objects/gameObjects.json")
        allEntities = characterFactory.buildSpriteObjects()
        camera = characterFactory.buildCamera(self.screenWidth, self.screenHeight)
        
        actionComponent = None
        for entity in allEntities:
            allSpriteList.add(entity)
            if entity._id == characterFactory.controllingEntityId:
                actionComponent = entity.actionComponent
        
        while not done:
            self.screen.fill(self.colors.BLACK)
            
            for entity in allEntities:
                entity.update()
                if entity._id == characterFactory.controllingEntityId:
                    camera.update(entity)
                entity.draw()
            
            for entity in allSpriteList:
                self.screen.blit(entity.image, camera.apply(entity))
            #allSpriteList.draw(self.screen)
            
            pygame.display.flip()
            self.clock.tick(60)
            done = actionComponent.endGame
        pygame.quit()
        
        
Game().start_game()