"""
    Default action component good for doing nothing.
"""
class BlankActionComponent:
    
    """
        Initializes the object.
    """
    def __init__(self, _id, desc):
        self._id = _id
        self.desc = desc

    """
        Runs the update to the logic component.
    """
    def update(self, actor, entity):
        entity.deltaX = 0
        entity.deltaY = 0