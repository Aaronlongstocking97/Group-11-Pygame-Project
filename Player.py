from GameSprites import *
from MainGame import *
from key import *
from body import *


class Player(GameSprite):

    def __init__(self, image_path, size, speed=5):
        super().__init__(image_path, speed, size=size)

        self.size = size
        self.set_position(500, 500)


        self.body = Body(PLAYER_IMAGE, BODY_SIZE)
        self.body.set_position(self.rect.x, self.rect.bottom)

        self.images = {
            "Right": pygame.image.load('assets/chararcter/character_right.png'),
            "Left": pygame.image.load('assets/chararcter/character_left.png'),
            "Down": pygame.image.load('assets/chararcter/character_front.png'),
            "Up": pygame.image.load('assets/chararcter/character_back.png')
        }

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def move(self):
        '''update method, allows player to move'''
        key_pressed = pygame.key.get_pressed(
        )  # Catch the key pressed event
        # (if pressed return True, else False)

        # Control the player
        if key_pressed[pygame.K_RIGHT]:
            self.image = self.images["Right"]
            self.image = pygame.transform.scale(self.image, self.size)
            self.rect.x += self.speed  # Right move
        elif key_pressed[pygame.K_LEFT]:
            self.image = self.images["Left"]
            self.image = pygame.transform.scale(self.image, self.size)
            self.rect.x -= self.speed  # Left mvoe
        elif key_pressed[pygame.K_UP]:
            self.image = self.images["Up"]
            self.image = pygame.transform.scale(self.image, self.size)
            self.rect.y -= self.speed  # Up move
        elif key_pressed[pygame.K_DOWN]:
            self.image = self.images["Down"]
            self.image = pygame.transform.scale(self.image, self.size)
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
        
        self.body.attach_player(self.rect.x, self.rect.bottom)

    # There may be a better way of doing this function
    def open_door(self, callback, key, door):
            if door.locked == True:
                # if this key is matching this door
                if type(key) == type(Key("assets/items/key.png", size=None)):
                    if key.door == door:
                        # remove key from bag's key group
                        callback.bag.keysGroup.remove(key)
                        # remove key for the bag list
                        callback.bag.items_list[callback.bag.index] = 0
                        # set next room to be the door's next room
                        next_room = door.next_room
                        door.locked = False
                        door.set_tip("You can open it!")
                        if next_room == "End":
                            callback.end_menu()
                        # switch
                        x, y = door.position_in_next_room
                        callback.player.set_position(x + 10, y + 30)
                        callback.switch_room(next_room)
                    else:
                        print("It is not the right key to use")
            elif door.locked == False:
                next_room = door.next_room
                x, y = door.position_in_next_room
                callback.player.set_position(x + 10, y + 30)
                callback.switch_room(next_room)

