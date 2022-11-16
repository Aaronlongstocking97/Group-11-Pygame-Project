from GameSprites import *
from item import *
# from Player import *
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
        # all the groups in room 1
        self.itemsGroup = pygame.sprite.Group()
        self.keysGroup = pygame.sprite.Group()
        self.doorGroup = pygame.sprite.Group()
        # self.walls = GameSprite(ROOM1WALLS, 0, (990,800))
        # self.walls.mask = pygame.mask.from_surface(self.walls.image)

    def addItemTo(self, item, position, group):
        return super().addItemTo(item, position, group)


class RoomTwo(Scene):

    def __init__(self, image):
        super().__init__(image)
        # all the groups in room 2
        self.itemsGroup = pygame.sprite.Group()
        self.keysGroup = pygame.sprite.Group()
        self.doorGroup = pygame.sprite.Group()

    def addItemTo(self, item, position, group):
        return super().addItemTo(item, position, group)
