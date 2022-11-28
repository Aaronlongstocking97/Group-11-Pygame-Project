from GameSprites import *
from bag import *


class Scene(GameSprite):

    def __init__(self, image):
        super().__init__(image)
        self.image = pygame.transform.scale(
            self.image, (SCREEN_RECT.width, SCREEN_RECT.height))
        self.itemsGroup = pygame.sprite.Group()
        self.keysGroup = pygame.sprite.Group()
        self.doorGroup = pygame.sprite.Group()
        self.pensGroup = pygame.sprite.Group()

    def addItemTo(self, item, position, group):
        group.add(item)
        x = position.x - 50
        y = position.y
        item.set_position(x, y)