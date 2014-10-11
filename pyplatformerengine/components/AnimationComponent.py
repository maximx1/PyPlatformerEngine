from pyplatformerengine.utilities.ImageUtils import ImageUtils

"""
    Default animation component for a platformer character.
"""
class AnimationComponent:
    
    """
        Initializes the object.
    """
    def __init__(self, animationProperties):
        self.props = animationProperties
    
    """
        Prepares the entity with its initial graphic.
    """
    def initializeCharacter(self, entity, startX, startY):
        imageUtils = ImageUtils(entity.spriteStages["standing"])
        entity.image = imageUtils.scale(self.props["width"], self.props["height"]).getImage()
        entity.rect = entity.image.get_rect()
        entity.rect.x = startX
        entity.rect.y = startY
        
    """
        Runs the update to the logic component.
    """
    def draw(self, entity):
        image = entity.spriteStages["standing"]
        imageUtils = ImageUtils(image)
        entity.image = imageUtils.scale(self.props["width"], self.props["height"]).getImage()
        originalX = entity.rect.x
        originalY = entity.rect.y
        entity.rect = entity.image.get_rect()
        entity.rect.x = originalX
        entity.rect.y = originalY