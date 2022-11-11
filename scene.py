from GameSprites import *
from item import *
from Player import *
from bag import *


class Scene(GameSprite):

    def __init__(self, image):
        super().__init__(image)
        self.image = pygame.transform.scale(
            self.image, (SCREEN_RECT.width, SCREEN_RECT.height))

    def addItemTo(self, item, position, group):
        group.add(item)
        x = position.x - 50
        y = position.y
        item.set_position(x, y)


class RoomOne(Scene):

    def __init__(self, image):
        super().__init__(image)
        self.itemsGroup = pygame.sprite.Group()
        self.keysGroup = pygame.sprite.Group()
        self.doorGroup = pygame.sprite.Group()

    def addItemTo(self, item, position, group):
        return super().addItemTo(item, position, group)


class RoomTwo(Scene):

    def __init__(self, image):
        super().__init__(image)
        self.itemsGroup = pygame.sprite.Group()
        self.keysGroup = pygame.sprite.Group()
        self.doorGroup = pygame.sprite.Group()

    def addItemTo(self, item, position, group):
        return super().addItemTo(item, position, group)
