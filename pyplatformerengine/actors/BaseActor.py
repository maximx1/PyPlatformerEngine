
"""
    Basic container class for an actor.
"""
class BaseActor:
    """
        Initializes the object with state variables.
    """
    def __init__(self, _id, name, description, components, stateDict):
        self._id = _id
        self.name = name
        self.description = description
        self.components = components
        self.stateDict = stateDict
        
    """
        Sets up all the components.
    """
    def setUp(self, entity):
        for component in self.components:
            if "setUp" in dir(component):
                component.setUp(self, entity)
    
    """
        Has the actor act out its part.
    """
    def act(self, entity):
        for component in self.components:
            component.update(self, entity)