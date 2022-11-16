from scene import *
from door import *
from key import *


class Hallway(Scene):

    def __init__(self, image):
        super().__init__(image)
        # all the groups in room 2
        self.itemsGroup = pygame.sprite.Group()
        self.keysGroup = pygame.sprite.Group()
        self.doorGroup = pygame.sprite.Group()

    def addItemTo(self, item, position, group):
        return super().addItemTo(item, position, group)

    def init_hallway(self, callback):
        callback.door_to_math = Door("assets/items/door.png", ITEM_SIZE)
        callback.door_to_math.init_door(
            self, callback.math_room, (500, 500), (910, 170))

        callback.key2 = Key("assets/items/key.png", ITEM_SIZE)
        callback.key2.init_key(self, callback.door_to_math, (400, 400),
                               "This is the key to open the math room door")
