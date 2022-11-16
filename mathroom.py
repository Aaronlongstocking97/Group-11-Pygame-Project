from scene import *
from math_generator import *
from door import *
from key import *

class MathRoom(Scene):

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

    def init_math_room(self, callback):
        self.questions = Generator("math_equations")

        callback.math_door = Door("assets/items/door.png", ITEM_SIZE)
        callback.math_door.init_door(self, callback.hallway, (910, 170), (500, 500))

        callback.key1 = Key("assets/items/key.png", ITEM_SIZE)
        callback.key1.init_key(self, callback.math_door, (400, 400),
                           "This is the key to enter the hallway")