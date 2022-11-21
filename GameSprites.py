import pygame
# from abc import ABC
# from abc import abstractmethod

# Game Global Constants
SCREEN_RECT = pygame.Rect(0, 0, 990, 800)
FRAME_RATE = 60
ITEM_SIZE = (60, 60)
DOOR_SIZE = (80, 95)
PLAYER_SIZE = (60, 80)
BODY_SIZE = (40, 30)

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
WHITE = (255, 255, 255)

BAG_IMAGE = "assets/items/bag.png"
HOVER_IMAGE = "assets/items/hover.png"
MATH_ROOM = "assets/rooms/mathroom.png"
MATH_ROOM_WALLS = "assets/rooms/mathroom_clutter.png"
HALLWAY = "assets/rooms/hallway.png"
HALLWAY_WALLS = "assets/rooms/hallway_mask.png"
LIBRARY = "assets/rooms/library.png"
LIBRARY_WALLS = "assets/rooms/library_mask.png"
BOX_IMAGE = "assets/items/box.png"
DOOR_IMAGE = "assets/rooms/door_closed.png"
KEY_IMAGE = "assets/items/key.png"
EQUATIONS_FILE_NAME = "math_equations"
SAFE_IMAGE = "assets/mathroom/safe-deposit.png"
GREEN_LIGHT = "assets/mathroom/check.png"
RED_LIGHT = "assets/mathroom/remove.png"
LOADING_LIGHT = "assets/mathroom/circle.png"
PENCIL_IMAGE = "assets/mathroom/pencil.png"
SCIENCE_ROOM = "assets/rooms/science_room.png"
SCIENCE_ROOM_WALLS = "assets/rooms/science_room_mask.png"
PLAYER_IMAGE = "assets/chararcter/character_front.png"


# class GameSprite(pygame.sprite.Sprite, ABC):


class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image_name, speed=1, size=None):

        super().__init__()
        self.image = pygame.image.load(image_name)
        if size != None:
            self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.mask = pygame.mask.from_surface(self.image)

    # @abstractmethod
    def update(self):
        pass
