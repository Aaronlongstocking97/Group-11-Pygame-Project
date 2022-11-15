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

    def set_description(self, description):
        return super().set_description(description)

    def init_key(self, room, door, position, description):
        x, y = position
        self.set_position(x, y)
        self.set_description(description)
        # this is to set this key is to be used for door 1
        self.set_matched_door(door)
        # add to the keys group of room1
        room.keysGroup.add(self)