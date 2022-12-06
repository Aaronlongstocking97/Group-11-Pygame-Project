from scene import *
from question_generator import *
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
        self.walls = GameSprite(MATH_ROOM_WALLS, 0, (990, 800))
        self.walls.mask = pygame.mask.from_surface(self.walls.image)
        # altered for testing purposes
        self.answers = 0
        self.passed = False

    def addItemTo(self, item, position, group):
        return super().addItemTo(item, position, group)

    def create_room(self, callback):
        self.questions = Generator(EQUATIONS_FILE_NAME)
        self.answer_box = AnswerBox(BOX_IMAGE, (100, 50))
        callback.math_door = Door(DOOR_IMAGE, DOOR_SIZE)
        self.loadingLight1 = Light(LOADING_LIGHT, (25, 25))

    def init_math_room(self, callback):

        self.ques, self.ans = self.questions.generate()

        callback.math_door.init_door(self, callback.hallway, (450, 600), (197, 185),
                                     "To the hallway")
        callback.math_door.locked = False

        # Create the loading lights on the white board

        self.loadingLight1.init_light(self, (330, 12))

    def display_question(self, callback):
        question_output = self.font.render(self.ques, True, BLACK)
        callback._screen.blit(question_output, (SCREEN_RECT.centerx - 30, 40))

    def reset_question(self):
        self.ques, self.ans = self.questions.generate()

    def pass_room(self, callback):
        callback.key_library = Key(KEY_IMAGE, ITEM_SIZE)
        callback.key_library.init_key(self, callback.door_to_library, (600, 400),
                                      "This is the key to open the library door")
