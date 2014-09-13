import pygame

from pyplatformerengine.utilities.Color import Color

class Game:
    
    colors = Color()
    
    def __init__(self):
        self.screen = pygame.display.set_mode((800,600))
        self.clock = pygame.time.Clock()
        
    def start_game(self):
        done = False
        pygame.init()
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                eventManager.determineEvents(event)
            self.screen.fill(self.colors.BLACK)
            
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()
        
        
game().start_game()