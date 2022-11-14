import pygame
from GameSprites import *
from item import *
from Player import Player
from bag import *
from scene import *
from door import *
from dialog import *


class MainGame(object):

    pygame.init()

    def __init__(self):
        self._screen = pygame.display.set_mode(SCREEN_RECT.size)
        self._clock = pygame.time.Clock()

        self.__create_sprites()

        self.current_room = None


    def startGame(self):

        self.current_room = self.room1

        while True:

            self._clock.tick(FRAME_RATE)

            self.__update_sprites()

            self.__event_handle()

            self.__collide_check()

            pygame.display.update()

    def __create_sprites(self):

        self.bag = Bag()
        self.player = Player("assets/chararcter/character_front.png", (60,80))
        self.room1 = RoomOne(ROOM1)
        self.room2 = RoomTwo(ROOM2)
        self.player.set_position(600, 600)

        self.dialog = Dialog()



        # The items in room one
        self.door1 = Door("assets/items/door.png", ITEM_SIZE)
        self.door1.set_position(910, 170)
        self.door1.set_next_room(self.room2)
        self.room1.doorGroup.add(self.door1)

        self.key1 = Key("assets/items/key.png", ITEM_SIZE)
        self.key1.set_position(400, 400)
        self.key1.set_matched_door(self.door1)
        self.room1.keysGroup.add(self.key1)

        self.item2 = Item("assets/items/key.png", ITEM_SIZE)
        self.item2.set_position(300, 300)
        self.room1.itemsGroup.add(self.item2)


        
       
        
        
        # The items in room two
        # self.item3 = Item("assets/items/key.png", ITEM_SIZE)
        # self.item3.set_position(200, 200)
        # self.item4 = Item("assets/items/key.png", ITEM_SIZE)
        # self.item4.set_position(300, 300)
        # self.item5 = Item("assets/items/key.png", ITEM_SIZE)
        # self.item5.set_position(400, 400)
        # self.item6 = Item("assets/items/key.png", ITEM_SIZE)
        # self.item6.set_position(100, 100)
        # self.item7 = Item("assets/items/key.png", ITEM_SIZE)
        # self.item7.set_position(50, 50)
        # self.item8 = Item("assets/items/key.png", ITEM_SIZE)
        # self.item8.set_position(250, 250)
        # self.item9 = Item("assets/items/key.png", ITEM_SIZE)
        # self.item9.set_position(200, 300)
        # self.item0 = Item("assets/items/key.png", ITEM_SIZE)
        # self.item0.set_position(200, 400)
        # self.key11 = Item("assets/items/key.png", ITEM_SIZE)
        # self.key11.set_position(200, 600)
        # self.key12 = Item("assets/items/key.png", ITEM_SIZE)
        # self.key12.set_position(200, 500)


        # self.room2.itemsGroup.add(self.item3)
        # self.room2.itemsGroup.add(self.item4)
        # self.room2.itemsGroup.add(self.item5)
        # self.room2.itemsGroup.add(self.item6)
        # self.room2.itemsGroup.add(self.item7)
        # self.room2.itemsGroup.add(self.item8)
        # self.room2.itemsGroup.add(self.item9)
        # self.room2.itemsGroup.add(self.item0)
        # self.room2.itemsGroup.add(self.key11)
        # self.room2.itemsGroup.add(self.key12)


    def __update_sprites(self):
        
        self.__draw_room(self.current_room)


        self._screen.blit(self.bag.bag_image, self.bag.bag_rect)
        self._screen.blit(self.bag.hover_image, self.bag.hover_rect)
        self._screen.blit(self.player.image, self.player.rect)

        self._screen.blit(self.dialog.image, self.dialog.rect)
        # self.dialog.display(self._screen)

        for item in self.bag.bagGroup:
            self._screen.blit(item.image, item.rect)
        for item in self.bag.keysGroup:
            self._screen.blit(item.image, item.rect)

        

        self.player.move()

    def __event_handle(self):
        events = pygame.event.get()
        for event in events:
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
                    # need to be changed
                    item = self.bag.items_list[self.bag.index]
                    if item != 0:
                        if type(item) == type(Key("assets/items/key.png", size=None)):
                            bag_group = self.bag.keysGroup
                            room_group = self.current_room.keysGroup
                        elif type(item) == type(Item("assets/items/key.png", size=None)):
                            bag_group = self.bag.bagGroup
                            room_group = self.current_room.itemsGroup
                        self.bag.put_item(item, bag_group)
                        self.current_room.addItemTo(item, self.player.rect, room_group)
                elif event.key == pygame.K_1:
                    # need to be changed
                    self.player.open_door(self, self.bag.items_list[self.bag.index])

    def __collide_check(self):
        # add item
        if self.bag.remain >0:
            collide = pygame.sprite.spritecollide(self.player, self.current_room.itemsGroup, False, pygame.sprite.collide_mask)
            if collide:
                for item in collide:
                    item.remove(self.current_room.itemsGroup)
                    self.bag.append_item(item, self.bag.bagGroup)

            collide = pygame.sprite.spritecollide(self.player, self.current_room.keysGroup, False, pygame.sprite.collide_mask)
            if collide:
                for item in collide:
                    item.remove(self.current_room.keysGroup)
                    self.bag.append_item(item, self.bag.keysGroup)

        # if the player can open a door or not
        
        
    def __draw_room(self, room):
        self._screen.blit(room.image, room.rect)
        for item in room.itemsGroup:
            self._screen.blit(item.image, item.rect)
        for door in room.doorGroup:
            self._screen.blit(door.image, door.rect)
        for key in room.keysGroup:
            self._screen.blit(key.image, key.rect)

    def switch_room(self, next_room):
        self.current_room = next_room


            

    def __quit_game(self):
        pygame.quit()
        exit()



