import pygame

class ActionComponent:
    endGame = False
    
    """
        Initializes the object with it's parent entity.
    """
    def __init__(self, entity, keyBindingMappings):
        self.entity = entity
        
    """
        Runs the update to the logic component.
    """
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.endGame = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.endGame = True
                elif event.key == pygame.K_LEFT:
                    print("Go Left")
                elif event.key == pygame.K_RIGHT:
                    print("Go Right")
                elif event.key == pygame.K_SPACE:
                    print("Jump")
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    print("Stop Going Left")
                elif event.key == pygame.K_RIGHT:
                    print("Stop Going Right")