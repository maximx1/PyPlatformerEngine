class AnimationComponent:
        
    """
        Runs the update to the logic component.
    """
    def draw(self, entity):
        entity.rect.x += entity.deltaX
        entity.rect.y += entity.deltaY