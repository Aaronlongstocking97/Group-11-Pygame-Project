from GameSprites import *

BAG_IMAGE = "assets/items/bag.png"
HOVER_IMAGE = "assets/items/hover.png"

class Bag(GameSprite):

    def __init__(self, speed=0):
        
        self.bag_image = pygame.image.load(BAG_IMAGE)
        self.hover_image = pygame.image.load(HOVER_IMAGE)
        self.bag_image = pygame.transform.scale(self.bag_image, (990, 110))

        self.hover_image = pygame.transform.scale(self.hover_image, (110, 110))

        self.bag_rect = self.bag_image.get_rect()
        self.hover_rect = self.hover_image.get_rect()
        self.bag_rect.y = self.hover_rect.y = SCREEN_RECT.bottom - self.bag_rect.height
        
        self.items_list = [0,0,0,0,0,0,0,0,0]
        self.index = 0
        self.bagGroup = pygame.sprite.Group()
        self.remain = 9

    def append_item(self, item):
        done = False
        next_space = 0
        while not done:
            if next_space > 8 or self.remain == 0:
                return
            if self.items_list[next_space] == 0:
                self.items_list[next_space] = item
                item.rect.y = self.bag_rect.y + 30
                item.rect.x = self.bag_rect.x + 25 + self.items_list.index(item) * 110
                self.bagGroup.add(item)
                self.remain -= 1
                done = True
            else: 
                next_space += 1

    def put_item(self, room, position):
        item = self.items_list[self.index]
        if item != 0:
            room.addItemTo(item, position)
            self.items_list[self.index] = 0
            item.remove(self.bagGroup)
            self.remain += 1
 


        
        
