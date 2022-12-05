from scene import *
from math_generator import *
from door import *
from key import *
from light import *

from answer_box import *


class ScienceRoom(Scene):

    def __init__(self, image):
        super().__init__(image)

        self.font = pygame.font.SysFont('timesnewroman', 20)

        self.itemsGroup = pygame.sprite.Group()
        self.keysGroup = pygame.sprite.Group()
        self.doorGroup = pygame.sprite.Group()
        self.lightsGroup = pygame.sprite.Group()
        self.pensGroup = pygame.sprite.Group()
        self.walls = GameSprite(SCIENCE_ROOM_WALLS, 0, (990, 800))
        self.walls.mask = pygame.mask.from_surface(self.walls.image)

        self.answers = 0
        self.passed = False

    def addItemTo(self, item, position, group):
        return super().addItemTo(item, position, group)

    def create_science_room(self, callback):
        callback.science_door = Door(DOOR_IMAGE, DOOR_SIZE)
        callback.key_exit = Key(KEY_IMAGE, ITEM_SIZE)
        self.loadingLight1 = Light(LOADING_LIGHT, (25, 25))
        self.questions = Generator(SCIENCE_ROOM_EQUATIONS_FILE_NAME)
        self.answer_box = AnswerBox(BOX_IMAGE, (100, 50))

    def init_science_room(self, callback):
        self.ques, self.ans = self.questions.generate()

        callback.science_door.init_door(self, callback.hallway, (30, 150), (455, 185),
                                        "To the hallway.")
        callback.science_door.locked = False

    def reset_question(self):
        self.ques, self.ans = self.questions.generate()

    def display_question(self, callback):
        question_output = self.font.render(self.ques, True, BLACK)
        callback._screen.blit(question_output, (550, 40))

    def pass_room(self, callback):
        callback.key_exit.init_key(self, callback.door_to_exit, (100, 300),
                                   "This is the key to escape")
