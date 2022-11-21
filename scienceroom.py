from scene import *
from math_generator import *
from door import *
from key import *
from light import *

from answer_box import *


class ScienceRoom(Scene):

    def __init__(self, image):
        super().__init__(image)
        # all the groups in room 1

        self.font = pygame.font.SysFont('timesnewroman', 30)

        self.itemsGroup = pygame.sprite.Group()
        self.keysGroup = pygame.sprite.Group()
        self.doorGroup = pygame.sprite.Group()
        self.lightsGroup = pygame.sprite.Group()
        self.pensGroup = pygame.sprite.Group()
        self.walls = GameSprite(SCIENCE_ROOM_WALLS, 0, (990,800))
        self.walls.mask = pygame.mask.from_surface(self.walls.image)


    def addItemTo(self, item, position, group):
        return super().addItemTo(item, position, group)

    def create_science_room(self, callback):
        callback.science_door = Door(DOOR_IMAGE, DOOR_SIZE)
        callback.key1 = Key(KEY_IMAGE, ITEM_SIZE)

    def init_science_room(self, callback):



        
        callback.science_door.init_door(self, callback.hallway, (30, 150), (455, 185),
                                "To the hallway.")
        callback.science_door.locked = False

        
        callback.key1.init_key(self, callback.science_door, (100, 300),
                           "This is the key to escape")



    def display_question(self, callback):
        question_output = self.font.render(self.ques, True, BLACK)
        callback._screen.blit(question_output, (SCREEN_RECT.centerx - 30, 40))


    def reset_question(self):
        self.ques, self.ans = self.questions.generate()