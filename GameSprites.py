import pygame
# from abc import ABC
# from abc import abstractmethod

# All the constants would be placed here
SCREEN_RECT = pygame.Rect(0, 0, 990, 800)
FRAME_RATE = 60
ITEM_SIZE = (60, 60)

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
WHITE = (255, 255, 255)

BAG_IMAGE = "assets/items/bag.png"
HOVER_IMAGE = "assets/items/hover.png"
ROOM1 = "assets/rooms/mathroom.png"
ROOM2 = "assets/background2.png"

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
