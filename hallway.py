from scene import *
from door import *
from key import *
from pen import *

class Hallway(Scene):

    def __init__(self, image):
        super().__init__(image)
        # all the groups in room 2
        self.itemsGroup = pygame.sprite.Group()
        self.keysGroup = pygame.sprite.Group()
        self.doorGroup = pygame.sprite.Group()
        self.pensGroup = pygame.sprite.Group()

    def addItemTo(self, item, position, group):
        return super().addItemTo(item, position, group)

    def init_hallway(self, callback):
        callback.door_to_math = Door(DOOR_IMAGE, ITEM_SIZE)
        callback.door_to_math.init_door(self, callback.math_room, (500, 500), (910, 170),
                                    "This door is locked, you might need a key.")

        callback.key2 = Key(KEY_IMAGE, ITEM_SIZE)
        callback.key2.init_key(self, callback.door_to_math, (400, 400),
                           "This is the key to open the math room door")

        callback.pencil = Pen(PENCIL_IMAGE, ITEM_SIZE)
        callback.pencil.init_pencil(self, (200, 200), "This is a pencil. You may use it to answer some questions")

