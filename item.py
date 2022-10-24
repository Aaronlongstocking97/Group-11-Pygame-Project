import pygame 
from GameSprites import GameSprite
# This is the item

class Item(GameSprite):

    def __init__(self, image_path, speed  = 0):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.font = 'freesansbold.ttf'
        self.font_size = 20
        self.text_color = (0, 0, 0)
        self.text_bg_color = (255, 255, 255)

    def set_size(self, size):
        '''Size the item image'''

        # Set the image size
        self.size = pygame.transform.scale(self.image, size)
    
    def set_description(self, description):

        # Set the description
        self.description = description

    def show_description(self):
        '''Show item description'''

        # Render the description on the window
        font = pygame.font.Font(self.font, self.font_size)
        return font.render(self.description, True, self.text_color, self.text_bg_color)






