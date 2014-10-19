from pyplatformerengine.utilities.ImageUtils import ImageUtils
from pyplatformerengine.utilities.LoggerUtil import LoggerUtil
from pyplatformerengine.entities.SpritesheetFactory import SpritesheetFactory

"""
    Default animation component for a platformer character.
"""
class AnimationComponent:
    
    """
        Initializes the object.
    """
    def __init__(self, _id, desc):
        self._id = _id
        self.desc = desc
    
    """
        Prepares the entity with its initial graphic.
    """
    def setUp(self, actor, entity):
        spritesheetFactory = SpritesheetFactory()
        actor.spriteStages = spritesheetFactory.createImages(actor.stateDict)
        imageUtils = ImageUtils(actor.spriteStages["standing"])
        entity.image = imageUtils.scale(actor.stateDict["animationProperties"]["width"], actor.stateDict["animationProperties"]["height"]).getImage()
        self.updateRect(entity)
        
    """
        Runs the update to the logic component.
    """
    def update(self, actor, entity):
        image = actor.spriteStages["standing"]
        imageUtils = ImageUtils(image)
        entity.image = imageUtils.scale(self.props["width"], self.props["height"]).getImage()
        self.updateRect(entity)
        loggerUtil = LoggerUtil()
        loggerUtil.info("CharacterLocation: (" + str(entity.rect.x) + ", " + str(entity.rect.y) + ")")
        
    """
        Updates the rectangle of the entity.
    """
    def updateRect(self, entity):
        originalX = entity.rect.x
        originalY = entity.rect.y
        entity.rect = entity.image.get_rect()
        entity.rect.x = originalX
        entity.rect.y = originalY