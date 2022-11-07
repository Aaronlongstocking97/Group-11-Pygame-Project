from GameSprites import *
from item import Item
from Player import Player
from bag import *
from item import Item
from background import *

ROOM1 = "assets/background.png"

class Background(GameSprite):

    def __init__(self):
        super().__init__(ROOM1)
        self.image = pygame.transform.scale(self.image, (SCREEN_RECT.width, SCREEN_RECT.height))
class RoomOne(Background):

    def __init__(self):
        super().__init__()
        self.itemsGroup = pygame.sprite.Group()


    def createRoomOne(self):

        self.item = Item("assets/items/key.png", ITEM_SIZE)
        self.item2 = Item("assets/items/key.png", ITEM_SIZE)
        self.item2.set_position(100, 100)

        self.item.set_position(400, 400)

        self.itemsGroup.add(self.item)
        self.itemsGroup.add(self.item2)

        
    def removeItemFrom(self, item):
        if item in self.itemsGroup:
            self.itemsGroup.remove(item)

    def addItemTp(self,item):
        self.itemsGroup.add(item)
            

    def DrawRoomOne(self, callback):
        callback._screen.blit(self.image, self.rect)
        for item in self.itemsGroup:
            callback._screen.blit(item.image, item.rect)
        print(self.itemsGroup)