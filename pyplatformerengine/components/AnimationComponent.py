class AnimationComponent:
        
    """
        Runs the update to the logic component.
    """
    def update(self, entity):
        entity.rect.x += entity.changeX
        entity.rect.y += entity.changeY