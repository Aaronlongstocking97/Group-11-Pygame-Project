from item import *


class Pen(Item):

    def __init__(self, image_path, size):
        super().__init__(image_path, size)

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def set_description(self, description):
        return super().set_description(description)

    def init_pencil(self, room, position, description):
        x, y = position
        self.set_position(x, y)
        self.set_description(description)
        # add to the keys group of room1
        room.pensGroup.add(self)