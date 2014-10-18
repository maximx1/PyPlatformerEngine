import pygame

"""
    Default controller for the platformer action component.
"""
class DefaultPlatformerActionComponent:
    """ 
        Runs the update to the logic component.
    """
    def update(self, actor, entity):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                actor.endGame = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    actor.endGame = True
                elif event.key == pygame.K_SPACE:
                    entity.initiateJump = True
    
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_LEFT]:
            entity.deltaX = -1 * actor.stateDict.get("leftRightMaxVelocity", 1)
        elif keys_pressed[pygame.K_RIGHT]:
            entity.deltaX = actor.stateDict.get("leftRightMaxVelocity", 1)
        else:
            entity.deltaX = 0
