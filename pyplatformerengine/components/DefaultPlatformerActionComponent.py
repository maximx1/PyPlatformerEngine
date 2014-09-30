import pygame

class DefaultPlatformerActionComponent:
    endGame = False
        
    """
        Runs the update to the logic component.
    """
    def determineAction(self, entity):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.endGame = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.endGame = True
                elif event.key == pygame.K_LEFT:
                    entity.deltaX = -1
                elif event.key == pygame.K_RIGHT:
                    entity.deltaX = 1
                elif event.key == pygame.K_SPACE:
                    entity.isJumping = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    entity.deltaX = 0
                elif event.key == pygame.K_RIGHT:
                    entity.deltaX = 0
                elif event.key == pygame.K_SPACE:
                    entity.isJumping = False