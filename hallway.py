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
        self.walls = GameSprite(HALLWAY_WALLS, 0, (990,800))
        self.walls.mask = pygame.mask.from_surface(self.walls.image)

    def addItemTo(self, item, position, group):
        return super().addItemTo(item, position, group)

    
    def creat_hallway(self, callback):
        callback.door_to_math = Door(DOOR_IMAGE, DOOR_SIZE)
        callback.key_mathroom = Key(KEY_IMAGE, ITEM_SIZE)
        callback.pencil = Pen(PENCIL_IMAGE, ITEM_SIZE)
        callback.door_to_library = Door(DOOR_IMAGE, DOOR_SIZE)
        callback.door_to_science = Door(DOOR_IMAGE, DOOR_SIZE)
        callback.door_to_exit = Door(DOOR_IMAGE, DOOR_SIZE)

    def init_hallway(self, callback):
        
        callback.door_to_math.init_door(self, callback.math_room, (197, 185), (450, 600),
                                    "Math room is locked, you might need a key.")
        
        callback.key_mathroom.init_key(self, callback.door_to_math, (400, 400),
                           "This is the key to open the math room door")

        callback.pencil.init_pencil(self, (300, 300), "This is a pencil. You may use it to answer some questions")
        
        callback.door_to_library.init_door(self, callback.library, (712, 185), (513, 600),
                                    "Library is locked, you might need a key.")

        callback.door_to_science.init_door(self, callback.science_room, (455, 185), (30, 150),
                                    "Science room is locked, you might need a key.")
        
        callback.door_to_exit.init_door(self, callback.winning_scene, (500, 500), (500, 500), "It's locked! You can't leave the school.")