from GameSprites import *
from item import *
from background import *

class Room(GameSprite):

    def __init__(self):
        super().__init__()
        self.items = []
        self.background = ""

    def set_item(self, item):
        pass