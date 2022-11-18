from GameSprites import *
from item import *
from key import *


class Bag(GameSprite):

    def __init__(self, speed=0):

        # image and size and ract
        self.bag_image = pygame.image.load(BAG_IMAGE)
        self.hover_image = pygame.image.load(HOVER_IMAGE)
        self.bag_image = pygame.transform.scale(self.bag_image, (990, 110))
        self.hover_image = pygame.transform.scale(self.hover_image, (110, 110))
        self.bag_rect = self.bag_image.get_rect()
        self.hover_rect = self.hover_image.get_rect()
        self.bag_rect.y = self.hover_rect.y = SCREEN_RECT.bottom - self.bag_rect.height

        # 0 means nothing in the index
        self.items_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        # the index player select
        self.index = 0
        # all groups in bag
        self.bagGroup = pygame.sprite.Group()
        self.keysGroup = pygame.sprite.Group()
        # how many items can be put in the bag
        self.remain = 9

    def append_item(self, item, group):
        done = False
        # Searches for the next avalible space in the bag
        next_space = 0
        while not done:
            # if the bag is full or the next avalible space is outside of
            # the bag size, then do nothing
            if next_space > 8 or self.remain == 0:
                return
            # if this equals to 0 meaning that this is the empty space
            if self.items_list[next_space] == 0:
                # put the item in this space
                self.items_list[next_space] = item
                # change the rect of this item to visully put it into the bag
                item.rect.y = self.bag_rect.y + 30
                item.rect.x = self.bag_rect.x + 25 + \
                    self.items_list.index(item) * 110

                # add it to the correct group
                group.add(item)
                # remain - 1
                self.remain -= 1
                done = True
            else:
                next_space += 1

    # remove an item from the correct group
    def remove_item(self, item, bag_group):
        # set this space to be 0
        self.items_list[self.index] = 0
        # remove from the correct bag group
        item.remove(bag_group)
        # remain + 1
        self.remain += 1

    def put_from_bag_event(self, callback):
        # Gets the item that the player chose (Consider Revising)
        item = self.items_list[self.index]
        if item != 0:
            # figure out what kind of item is it, if it is a key type, then it would be set to/remove from keys group.
            # As items getting more and more, we can encapsulate this into a function
            if type(item) == type(Key("assets/items/key.png", size=None)):
                bag_group = self.keysGroup
                room_group = callback.current_room.keysGroup
            elif type(item) == type(Item("assets/items/key.png", size=None)):
                bag_group = self.bagGroup
                room_group = callback.current_room.itemsGroup
            self.remove_item(item, bag_group)
            callback.current_room.addItemTo(
                item, callback.player.rect, room_group)

    def move_hover_left(self):
        if self.index > 0:
            self.hover_rect.x -= 110
            self.index -= 1

    def move_hover_right(self):
        if self.index < 8:
            self.hover_rect.x += 110
            self.index += 1