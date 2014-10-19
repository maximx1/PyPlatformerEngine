
"""
    Basic container class for an actor.
"""
class BaseActor:
    """
        Initializes the object with state variables.
    """
    def __init__(self, _id, name, components, stateDict):
        self._id = _id
        self.name = name
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
            
    """
        Hashing function for using as key
    """
    def __hash__(self):
        return hash((self._id, self.name))

    """
        Equality Checker.
    """
    def __eq__(self, other):
        return (self._id, self.name) == (other._id, other.name)