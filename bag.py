from GameSprites import *

BAG_IMAGE = "bomb.png"
HOVER_IMAGE = "bomb.png"

class Bag(GameSprite):

    def __init__(self, speed=0):
        
        self.bag_image = pygame.image.load(BAG_IMAGE)
        self.hover_image = pygame.image.load(HOVER_IMAGE)
        self.bag_rect = self.bag_image.get_rect()
        self.hover_rect = self.hover_image.get_rect()
        self.bag_rect.y = self.hover_rect.y = SCREEN_RECT.bottom - self.bag_rect.height

        self.items_list = []
        self.index = 0

    def append_item(self, item):
        self.items_list.append(item)
        item.rect.y = SCREEN_RECT.bottom
        item.rect.x = self.bag_rect + self.items_list.index(item) * 50

    def use_item(self, hero_rect):
        item = self.items_list.pop(self.index)
        item.rect = hero_rect
        return item



        
        
