from item import *


class Light(Item):

    def __init__(self, image_path, size):
        super().__init__(image_path, size)

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def usage(self):
        pass

    def init_light(self, room, position):
        x, y = position
        self.set_position(x, y)
        # add to the light group of room1
        room.lightsGroup.add(self)

    def wrong_answer(self):
        self.image = pygame.image.load(RED_LIGHT)
        self.image = pygame.transform.scale(self.image, (25 ,25))
        self.rect.x = 330
        self.rect.y = 12

    def right_answer(self):
        self.image = pygame.image.load(GREEN_LIGHT)
        self.image = pygame.transform.scale(self.image, (25 ,25))
        self.rect.x = 330
        self.rect.y = 12