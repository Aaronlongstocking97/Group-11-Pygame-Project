import pygame

# All the constants would be placed here
SCREEN_RECT = pygame.Rect(0,0,990,800)
FRAME_RATE = 60
ITEM_SIZE= (60, 60)


BLACK = (0,0,0)
GREEN = (0,255,0)

class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image_name, speed=1, size = None):

        super().__init__()
        self.image = pygame.image.load(image_name)
        if size != None:
            self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.mask = pygame.mask.from_surface(self.image)

    # Sprite has a methoed called update. When you call this function in a sprite gropu, it will call the update methoed for all the objects in this group
    def update(self):
        pass