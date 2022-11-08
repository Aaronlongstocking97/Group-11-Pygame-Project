import pygame
from GameSprites import *
from item import Item
from Player import Player
from bag import *
from item import Item
from sence import *


class MainGame(object):

    pygame.init()

    def __init__(self):
        self._screen = pygame.display.set_mode(SCREEN_RECT.size)
        self._clock = pygame.time.Clock()

        self.__create_sprites()

        # self.room1Display = True
        # self.room2Display = False
        # self.room3Display = False
        # self.room4Display = False
        # self.room5Display = False

        self.current_room = None


    def startGame(self):

        while True:

            self._clock.tick(FRAME_RATE)

            self.__update_sprites()

            self.__event_handle()

            self.__collide_check()

            pygame.display.update()

    def __create_sprites(self):

        self.bag = Bag()
        self.player = Player("assets\chararcter\character_temp.png", (60,80))
        self.room1 = RoomOne(ROOM1)
        self.room2 = RoomTwo(ROOM2)
        self.player.set_position(600, 600)


        # The items in room one
        self.item = Item("assets/items/key.png", ITEM_SIZE)
        self.item2 = Item("assets/items/key.png", ITEM_SIZE)
        self.item2.set_position(100, 100)
        self.item.set_position(400, 400)

        self.room1.itemsGroup.add(self.item)
        self.room1.itemsGroup.add(self.item2)
        
        # The items in room two
        self.item3 = Item("assets/items/key.png", ITEM_SIZE)
        self.item3.set_position(200, 200)
        self.item4 = Item("assets/items/key.png", ITEM_SIZE)
        self.item4.set_position(300, 300)
        self.item5 = Item("assets/items/key.png", ITEM_SIZE)
        self.item5.set_position(400, 400)
        self.item6 = Item("assets/items/key.png", ITEM_SIZE)
        self.item6.set_position(100, 100)
        self.item7 = Item("assets/items/key.png", ITEM_SIZE)
        self.item7.set_position(50, 50)
        self.item8 = Item("assets/items/key.png", ITEM_SIZE)
        self.item8.set_position(250, 250)
        self.item9 = Item("assets/items/key.png", ITEM_SIZE)
        self.item9.set_position(200, 300)
        self.item0 = Item("assets/items/key.png", ITEM_SIZE)
        self.item0.set_position(200, 400)
        self.item11 = Item("assets/items/key.png", ITEM_SIZE)
        self.item11.set_position(200, 600)
        self.item12 = Item("assets/items/key.png", ITEM_SIZE)
        self.item12.set_position(200, 500)


        self.room2.itemsGroup.add(self.item3)
        self.room2.itemsGroup.add(self.item4)
        self.room2.itemsGroup.add(self.item5)
        self.room2.itemsGroup.add(self.item6)
        self.room2.itemsGroup.add(self.item7)
        self.room2.itemsGroup.add(self.item8)
        self.room2.itemsGroup.add(self.item9)
        self.room2.itemsGroup.add(self.item0)
        self.room2.itemsGroup.add(self.item11)
        self.room2.itemsGroup.add(self.item12)


    def __update_sprites(self):
        # if self.room1Display:
        #     self.__draw_room(self.room1)
        #     self.current_room = self.room1
        # if self.room2Display:
        #     self.__draw_room(self.room2)
        self.__draw_room(self.current_room)
        # if self.room3Display:
        #     pass
        # if self.room4Display:
        #     pass
        # if self.room5Display:
        #     pass      

        self._screen.blit(self.bag.bag_image, self.bag.bag_rect)
        self._screen.blit(self.bag.hover_image, self.bag.hover_rect)
        self._screen.blit(self.player.image, self.player.rect)
        for item in self.bag.items_list:
            if item != 0:
                self._screen.blit(item.image, item.rect)

        self.player.move()

    def __event_handle(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    if self.bag.index > 0:
                        self.bag.hover_rect.x -= 110
                        self.bag.index -= 1
                elif event.key == pygame.K_d:
                    if self.bag.index < 8:
                        self.bag.hover_rect.x += 110
                        self.bag.index += 1
                elif event.key == pygame.K_SPACE:
                    self.bag.put_item(self.current_room, self.player.rect)

    def __collide_check(self):
        # add item
        if self.bag.remain >0:
            collide = pygame.sprite.spritecollide(self.player, self.current_room.itemsGroup, False, pygame.sprite.collide_mask)
            if collide:
                for item in collide:
                    item.remove(self.current_room.itemsGroup)
                    self.bag.append_item(item)
                    print(self.bag.bagGroup)
                    self.__switch_room()

    def __draw_room(self, room):
        self._screen.blit(room.image, room.rect)
        for item in room.itemsGroup:
            self._screen.blit(item.image, item.rect)

    def __switch_room(self):
        self.room1Display = False
        self.room2Display = True
    def __quit_game(self):
        pygame.quit()
        exit()


def main():

    start = MainGame()

    start.startGame()


if __name__ == "__main__":
    main()
