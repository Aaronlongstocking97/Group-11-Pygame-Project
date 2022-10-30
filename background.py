from GameSprites import *

IMAGE_NAME = "assets/background.png"

class Background(GameSprite):

    def __init__(self):
        super().__init__(IMAGE_NAME)
        self.image = pygame.transform.scale(self.image, (SCREEN_RECT.width, SCREEN_RECT.height))
