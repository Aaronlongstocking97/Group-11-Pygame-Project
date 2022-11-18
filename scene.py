from GameSprites import *
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