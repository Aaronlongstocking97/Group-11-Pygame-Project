from scene import *
# from math_generator import *
from door import *
from key import *
from light import *

from answer_box import *


class Library(Scene):

    def __init__(self, image):
        super().__init__(image)
        # all the groups in room 1

        self.font = pygame.font.SysFont('timesnewroman', 30)

        self.itemsGroup = pygame.sprite.Group()
        self.keysGroup = pygame.sprite.Group()
        self.doorGroup = pygame.sprite.Group()
        self.lightsGroup = pygame.sprite.Group()
        self.pensGroup = pygame.sprite.Group()
        # self.walls = GameSprite(ROOM1WALLS, 0, (990,800))
        # self.walls.mask = pygame.mask.from_surface(self.walls.image)


    def addItemTo(self, item, position, group):
        return super().addItemTo(item, position, group)

    def create_library(self, callback):
        callback.library_door = Door(DOOR_IMAGE, DOOR_SIZE)
        callback.key_science = Key(KEY_IMAGE, ITEM_SIZE)

    def init_library(self, callback):


        
        callback.library_door.init_door(self, callback.hallway, (513, 600), (712, 185),
                                "This door is locked, you might need a key.")
        callback.library_door.locked = False

        
        callback.key_science.init_key(self, callback.door_to_science, (500, 500), "This is the key to science")


    def display_question(self, callback):
        question_output = self.font.render(self.ques, True, BLACK)
        callback._screen.blit(question_output, (SCREEN_RECT.centerx - 30, 40))


    def reset_question(self):
        self.ques, self.ans = self.questions.generate()

