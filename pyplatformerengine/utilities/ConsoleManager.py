"""
    The backend for the in-game console management scripting. 
"""
class ConsoleManager:
    _instance  = None
    allEntities = {}
    inScopeEntities = {}
    
    """
        Turns new into a singleton retriever.
    """
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ConsoleManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    """
        Adds list of entities to the master entity list. overwrites stuff with the same _id.
    """
    def addToMasterEntityList(self, entityList):
        for entity in entityList:
            self.allEntities[entity._id] = entity
        
    """
        Removes and item from the master list.
    """
    def removeEntityFromMasterList(self, _id):
        del self.allEntities[_id]
        
    """
        Sets the current in scope entities.
    """
    def setInScopeEntities(self, entityList):
        for entity in entityList:
            self.inScopeEntities[entity._id] = entity
            
    """
        Gets the list of in scope entities.
    """
    def getInScopeEntities(self):
        return self.inScopeEntities.values()
    
    """
        Overrides the location of an entity.
    """
    def setLocation(self, _id, newX, newY):
        for entity in self.inScopeEntities:
            if entity._id == _id:
                entity.rect.x
    
    """
        Plugin to run custom function across the entities.
    """
    def runCustomFunctionOnAllEntities(self, customFunction):
        customFunction(self.allEntities)
        
    """
        Plugin to run custom function across the in scope entities.
    """
    def runCustomFunctionOnInScopeEntities(self, customFunction):
        customFunction(self.inScopeEntities)