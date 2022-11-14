from item import *


class Key(Item):

    def __init__(self, image_path, size):
        super().__init__(image_path, size)

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def set_matched_door(self, door):
        self.door = door

    def usage(self):
        pass
