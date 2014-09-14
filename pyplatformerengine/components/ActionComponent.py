class ActionComponent:
    """
        Initializes the object with it's parent entity.
    """
    def __init__(self, entity):
        self.entity = entity
        
    """
        Runs the update to the logic component.
    """
    def update(self):
        print("Default input controls")