"""
    Manager to detect proximity.
"""
class ProximityManager:
    
    """
        Initializes the object.
    """
    def __init__(self, entities):
        self.entities = entities

    """
        Detects the proximity to other objects.
    """
    def checkProximityToPlayers(self, entities):
        for entity in entities:
            entity.proximityEventActivated = False
        for pEntity in self.entities:
            playerRadius, playerX, playerY = self.calculateObjectRadiusAndCenterpoint(pEntity)
            for entity in entities:
                if not entity.proximityEventActivated:
                    entityRadius, entityX, entityY = self.calculateObjectRadiusAndCenterpoint(entity)
                    entityRadius = max(entityRadius, entity.proximityThreshold)
                    entity.proximityEventActivated = self.determineIfObjectsAreInVicinity(playerX, playerY, playerRadius, entityX, entityY, entityRadius)                    

    """
        Calculates an objects radius and centerpoint.
    """
    def calculateObjectRadiusAndCenterpoint(self, entity):
        halfHeight = (int)(entity.iHeight / 2)
        halfWidth = (int)(entity.iWidth / 2)
        radius = (int)(((halfHeight ** 2) + (halfWidth ** 2)) ** .5)
        newX, newY = (entity.rect.x + halfHeight, entity.rect.y + halfWidth)
        return (radius, newX, newY)
    
    
    
    def determineIfObjectsAreInVicinity(self, entity1X, entity1Y, entity1Radius, entity2X, entity2Y, entity2Radius):
        distance = ((((entity1X - entity2X) ** 2) + ((entity1Y - entity2Y) ** 2)) ** .5)
        combinedRadii = entity1Radius + entity2Radius
        return True if combinedRadii > distance else False