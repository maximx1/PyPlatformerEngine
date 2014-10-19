from pyplatformerengine.utilities.ClassLoaderUtils import ClassLoaderUtils
from pyplatformerengine.actors.BaseActor import BaseActor
from pyplatformerengine.utilities.ConsoleManager import ConsoleManager
class ActorFactory:
    
    """
        Builds the components for the actors.
    """
    def buildComponents(self, componentDefinitions):
        classLoader = ClassLoaderUtils()
        components = []
        for component in componentDefinitions:
            components.append(classLoader.importClass(component["componentModule"], component["componentClass"])(component["_id"], component["desc"]))
        return components
    
    """
        Builds an actor
    """
    def buildActors(self, actorDefinitions, availableComponents):
        updateActors = []
        drawActors = [] 
        for actorDefinition in actorDefinitions["updateActors"]:
            updateActors.append(self.buildActor(actorDefinition, availableComponents))
        for actorDefinition in actorDefinitions["drawActors"]:
            drawActors.append(self.buildActor(actorDefinition, availableComponents))
        return updateActors, drawActors
        
    """
        Assembles a single actor.
    """
    def buildActor(self, actorDefinition, availableComponents):
        _id = actorDefinition["_id"]
        name = actorDefinition["name"]
        controllingEntity = False if actorDefinition.get("controllingEntity", 0) == 0 else True
        stateDict = actorDefinition.get("state", None)
        
        #Add components
        componentsToAdd = []
        for componentDefinition in actorDefinition["components"]:
            for availableComponent in availableComponents:
                if availableComponent._id == componentDefinition:
                    componentsToAdd.append(availableComponent)
                    
        actor =  BaseActor(_id, name, componentsToAdd, stateDict)
        if controllingEntity:
            ConsoleManager().controllingActor = actor