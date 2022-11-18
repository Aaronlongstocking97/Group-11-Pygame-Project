from GameSprites import *


class Item(GameSprite):

    def __init__(self, image_path, size):
        super().__init__(image_path, speed=0, size=size)
        self.font = pygame.font.SysFont('timesnewroman', 20)
        self.description = ""
        self.tip = ""

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def set_size(self, size):
        '''Size the item image'''

        # Set the image size
        self.image = pygame.transform.scale(self.image, size)

    def set_description(self, description):

        # Set the description
        self.description = description

    def show_tip(self, callback):
        '''Show item description'''

        # Render the description on the window
        tip = self.font.render(self.tip, True, BLACK, WHITE)
        callback._screen.blit(tip, (20, 650))

    def set_tip(self, tip):
        self.tip = tip
