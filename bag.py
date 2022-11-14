from GameSprites import *
from item import *


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
        # this is to find out what is the next avalible space in the bag
        next_space = 0
        while not done:
            # if the bag is full or the next avalible space is outside of the bag size, then do nothing
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

                # add it into the correct group
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
