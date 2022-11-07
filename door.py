import pygame
from item import Item

class Door(Item):
    def __init__(self, image_path, size):
        super().__init__(image_path, size)

    def open_door(self, no_key = False):
        if not no_key:
            return "door (1).png"

    def next_room(self):
        return pygame.Rect(0,0,990,800)

            
        
