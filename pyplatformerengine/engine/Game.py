import pygame

from pyplatformerengine.utilities import Color
from pyplatformerengine.entities.CharacterFactory import CharacterFactory

class Game:
    
    colors = Color.Color()
    
    def __init__(self):
        self.screen = pygame.display.set_mode((800,600))
        self.clock = pygame.time.Clock()
        
    def start_game(self):
        done = False
        pygame.init()
        
        allSpriteList = pygame.sprite.Group()
        characterFactory = CharacterFactory("../../resources/gameObjects.json")
        allEntities = characterFactory.buildSpriteObjects()
        
        actionComponent = None
        for entity in allEntities:
            allSpriteList.add(entity)
            if entity._id == characterFactory.controllingEntityId:
                actionComponent = entity.actionComponent
        
        while not done:
            self.screen.fill(self.colors.BLACK)
            
            for entity in allEntities:
                entity.update()
                entity.draw()
            
            allSpriteList.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)
            done = actionComponent.endGame
        pygame.quit()
        
        
Game().start_game()