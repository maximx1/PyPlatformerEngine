import pygame

from pyplatformerengine.utilities import Color
from pyplatformerengine.components import *
from pyplatformerengine.entities import *

class Game:
    
    colors = Color.Color()
    
    def __init__(self):
        self.screen = pygame.display.set_mode((800,600))
        self.clock = pygame.time.Clock()
        
    def start_game(self):
        done = False
        pygame.init()
        actionComponent = DefaultPlatformerActionComponent.DefaultPlatformerActionComponent()
        animationComponent = AnimationComponent.AnimationComponent()
        physicsComponent = PhysicsComponent.PhysicsComponent(1)
        allSpriteList = pygame.sprite.Group()
        character = Character.Character(actionComponent, animationComponent, physicsComponent)
        allSpriteList.add(character)
        while not done:
            self.screen.fill(self.colors.BLACK)
            
            character.update()
            character.draw()
            
            allSpriteList.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)
            done = actionComponent.endGame
        pygame.quit()
        
        
Game().start_game()