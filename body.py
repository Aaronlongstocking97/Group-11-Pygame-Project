from GameSprites import *



class Body(GameSprite):

    def __init__(self, image_name, size):
        super().__init__(image_name, size=size)


    def attach_player(self, x, y):
        self.rect.x = x
        self.rect.bottom = y

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y