from scene import *
from question_generator import *
from door import *
from key import *
from light import *
from answer_box import *


class Library(Scene):

    def __init__(self, image):
        super().__init__(image)
        # all the groups in room 2

        self.font = pygame.font.SysFont('timesnewroman', 30)

        self.itemsGroup = pygame.sprite.Group()
        self.keysGroup = pygame.sprite.Group()
        self.doorGroup = pygame.sprite.Group()
        self.lightsGroup = pygame.sprite.Group()
        self.pensGroup = pygame.sprite.Group()
        self.walls = GameSprite(LIBRARY_WALLS, 0, (990, 800))
        self.walls.mask = pygame.mask.from_surface(self.walls.image)

        self.answers = 0  # added and needs to be connected to other variables
        self.passed = False  # added and needs to be connected to other variables

    def addItemTo(self, item, position, group):
        return super().addItemTo(item, position, group)

    def create_library(self, callback):
        callback.library_door = Door(DOOR_IMAGE, DOOR_SIZE)
        # changed wording and needs to be connected to other variables
        callback.key_library = Key(KEY_IMAGE, ITEM_SIZE)
        # callback.key_science = Key(KEY_IMAGE, ITEM_SIZE)

    def init_library(self, callback):

        # added and needs to be connected to other variables
        self.ques, self.ans = self.questions.generate()

        callback.library_door.init_door(self, callback.hallway, (513, 600), (712, 185),
                                        "To the hallway.")
        callback.library_door.locked = False

        # Creates the loading lights on the white board

        # added and needs to be connected to other variables
        self.loadingLight1.init_light(self, (330, 12))

        # callback.key_science.init_key(
        #     self, callback.door_to_science, (500, 500), "This is the key to science")

    def display_question(self, callback):
        question_output = self.font.render(self.ques, True, BLACK)
        callback._screen.blit(question_output, (SCREEN_RECT.centerx - 30, 40))

    def reset_question(self):
        self.ques, self.ans = self.questions.generate()

    # added and needs to be connected to other variables
    def pass_room(self, callback):
        callback.key_library = Key(KEY_IMAGE, ITEM_SIZE)
        callback.key_library.init_key(self, callback.door_to_library, (600, 400),
                                      "This is the key to open the science door")
