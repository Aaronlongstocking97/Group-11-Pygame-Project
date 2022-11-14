
import time
import pygame
from GameSprites import *



class Item(GameSprite):

    def __init__(self, image_path, size):
        super().__init__(image_path, speed=0, size=size)
        self.font = 'freesansbold.ttf'
        self.font_size = 20
        self.text_color = (0, 0, 0)
        self.text_bg_color = (255, 255, 255)
        self.size = size

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def set_size(self):
        '''Size the item image'''

        # Set the image size
        self.image = pygame.transform.scale(self.image, self.size)
    def set_description(self, description):

        # Set the description
        self.description = description

    def show_description(self, window_width, window_height):
        '''Show item description'''

        # Render the description on the window
        font = pygame.font.Font('freesansbold.ttf', self.font_size)
        text = font.render(self.description, True,
                           self.text_color, self.text_bg_color)
        text_rect = text.get_rect()
        text_rect.center = (window_width, window_height)

    def usage(self):
        pass

    def pick_up(self, jump = False):
        vel_y = 10

        if jump:
            self.rect.y -= vel_y # Go up
            vel_y -= 1 # Go down
            print("jump")
            pygame.time.wait(100)
            if vel_y < -5:
                jump = False
                vel_y = 10
                print("jumped")
            pygame.time.wait(240)

class Key(Item):

    def __init__(self, image_path, size):
        super().__init__(image_path, size)
    
    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    # set the door that can be used with this key
    def set_matched_door(self, door):
        self.door = door

    def usage(self):
        pass
