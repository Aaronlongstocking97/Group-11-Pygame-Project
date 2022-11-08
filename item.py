import pygame 
from GameSprites import GameSprite

class Item(GameSprite):

    def __init__(self, image_path, size):
        super().__init__(image_path, speed  = 0, size = size)
        self.font = 'freesansbold.ttf'
        self.font_size = 20
        self.text_color = (0, 0, 0)
        self.text_bg_color = (255, 255, 255)

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

    def show_description(self, window_width, window_height):
        '''Show item description'''

        # Render the description on the window
        font = pygame.font.Font('freesansbold.ttf', self.font_size)
        text = font.render(self.description, True, self.text_color, self.text_bg_color)
        text_rect = text.get_rect()
        text_rect.center = (window_width, window_height)






