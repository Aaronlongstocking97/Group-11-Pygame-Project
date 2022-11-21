from scene import *
from math_generator import *
from door import *
from key import *
from light import *

from answer_box import *


class MathRoom(Scene):

    def __init__(self, image):
        super().__init__(image)
        # all the groups in room 1

        self.font = pygame.font.SysFont('timesnewroman', 30)

        self.itemsGroup = pygame.sprite.Group()
        self.keysGroup = pygame.sprite.Group()
        self.doorGroup = pygame.sprite.Group()
        self.lightsGroup = pygame.sprite.Group()
        self.pensGroup = pygame.sprite.Group()
        self.walls = GameSprite(MATH_ROOM_WALLS, 0, (990,800))
        self.walls.mask = pygame.mask.from_surface(self.walls.image)


    def addItemTo(self, item, position, group):
        return super().addItemTo(item, position, group)

    def init_math_room(self, callback):

        self.questions = Generator(EQUATIONS_FILE_NAME)
        self.ques, self.ans = self.questions.generate()

        self.answer_box = AnswerBox(BOX_IMAGE, (100, 50))

        callback.math_door = Door(DOOR_IMAGE, DOOR_SIZE)
        callback.math_door.init_door(self, callback.hallway, (800, 40), (197, 185),
                                "This door is locked, you might need a key.")

        callback.key1 = Key(KEY_IMAGE, ITEM_SIZE)
        callback.key1.init_key(self, callback.math_door, (400, 400),
                           "This is the key to enter the hallway")

        # Create the loading lights on the white board
        self.loadingLight1 = Light(LOADING_LIGHT, (25 ,25))
        self.loadingLight1.init_light(self, (330, 12))

    def display_question(self, callback):
        question_output = self.font.render(self.ques, True, BLACK)
        callback._screen.blit(question_output, (SCREEN_RECT.centerx - 30, 40))


    def reset_question(self):
        self.ques, self.ans = self.questions.generate()

