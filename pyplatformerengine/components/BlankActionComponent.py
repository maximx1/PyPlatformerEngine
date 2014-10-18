"""
    Default action component good for doing nothing.
"""
class BlankActionComponent:

    """
        Runs the update to the logic component.
    """
    def update(self, actor, entity):
        entity.deltaX = 0
        entity.deltaY = 0