import pygame
from GameSprites import GameSprite
from item import *


class Player(GameSprite):

    def __init__(self, image_path, size, speed=3):
        super().__init__(image_path, speed, size=size)

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def move(self):
        '''update method, allows player to move'''
        key_pressed = pygame.key.get_pressed(
        )  # Catch the key pressed event (if pressed return True, else False)

        # Control the player
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speed  # Right move
        elif key_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speed  # Left mvoe
        elif key_pressed[pygame.K_UP]:
            self.rect.y -= self.speed  # Up move
        elif key_pressed[pygame.K_DOWN]:
            self.rect.y += self.speed  # Down move

        # Limit the player in the window screen
        if self.rect.right > 990:
            self.rect.right = 990
        elif self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > 700:
            self.rect.bottom = 700

    def open_door(self, callback, key):
        collide = pygame.sprite.spritecollide(
            callback.player, callback.current_room.doorGroup, False, pygame.sprite.collide_mask)
        if collide:
            for door in collide:
                if type(key) == type(Key("assets/items/key.png", size=None)):
                    if key.door == door:
                        callback.bag.keysGroup.remove(key)
                        callback.bag.items_list[callback.bag.index] = 0
                        next_room = door.next_room
                        callback.switch_room(next_room)
                    else:
                        print("It is not the right item to use")
