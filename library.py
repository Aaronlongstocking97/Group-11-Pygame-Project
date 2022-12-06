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
        self.pensGroup = pygame.sprite.Group()  # This isn't necessary
        self.walls = GameSprite(LIBRARY_WALLS, 0, (990, 800))
        self.walls.mask = pygame.mask.from_surface(self.walls.image)
        # altered for testing purposes
        self.answers = 5
        self.passed = False

    def addItemTo(self, item, position, group):
        return super().addItemTo(item, position, group)

    def create_library(self, callback):
        callback.library_door = Door(DOOR_IMAGE, DOOR_SIZE)
        self.questions = Generator(SPELLING_WORDS_FILE_NAME)
        self.answer_box = AnswerBox(BOX_IMAGE, (100, 50))
        # Changing these values (answer_box, loadingLight1) will only
        # increase the size of the object not the location.
        self.loadingLight1 = Light(LOADING_LIGHT, (25, 25))

    def init_library(self, callback):

        self.ques, self.ans = self.questions.generate()

        callback.library_door.init_door(self, callback.hallway, (513, 600), (712, 185),
                                        "To the hallway.")
        callback.library_door.locked = False

        # Creates the loading lights on the white board

        # added and needs to be placed in the correct position.
        self.loadingLight1.init_light(self, (330, 100))
        self.answer_box.init_answer_box(self, (450, 200))

    def display_question(self, callback):
        question_output = self.font.render(self.ques, True, BLACK)
        callback._screen.blit(question_output, (SCREEN_RECT.centerx - 88, 130))

    def reset_question(self):
        self.ques, self.ans = self.questions.generate()

    def pass_room(self, callback):
        callback.key_science = Key(KEY_IMAGE, ITEM_SIZE)
        callback.key_science.init_key(self, callback.door_to_science, (600, 400),
                                      "This is the key to open the science door")
