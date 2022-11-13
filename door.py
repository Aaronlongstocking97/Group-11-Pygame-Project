import pygame
from item import Item

class Door(Item):
    def __init__(self, image_path, size):
        super().__init__(image_path, size)

    # this need to be change
    def open_door(self, no_key = False):
        if not no_key:
            return "assets/items/door (1).png"
        else:
            return "assets/items/door.png"

    # set the next room of this door
    def set_next_room(self, room):
        self.next_room = room

            
        
