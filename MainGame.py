import pygame
from GameSprites import *
from item import *
from Player import Player
from bag import *
from scene import *
from door import *
from dialog import *
from key import *

# Does this still need to take in an object?


class MainGame(object):

    pygame.init()

    def __init__(self):
        # main screen
        self._screen = pygame.display.set_mode(SCREEN_RECT.size)
        self._clock = pygame.time.Clock()
        # create all the sprites and put them in the right
        # position plus right group
        self.__create_sprites()

        # This is a pointer to point the current room the player is in.
        self.current_room = None

    def startGame(self):
        # Set the current room to the first room in the game.
        self.current_room = self.room1

        while True:
            # frame rate 60 hz
            self._clock.tick(FRAME_RATE)

            self.__update_sprites()

            self.__event_handle()

            self.__collide_check()

            pygame.display.update()

    def __create_sprites(self):
        # create the bag
        self.bag = Bag()
        # create the player and set the position of player(testing)
        self.player = Player("assets/chararcter/character_front.png", (60, 80))
        self.player.set_position(600, 600)
        # Create the first room
        self.room1 = RoomOne(ROOM1)
        # Create the second room
        self.room2 = RoomTwo(ROOM2)
        # Add a spice of dialog to the mix
        self.dialog = Dialog()

        self.door2 = Door("assets/items/door.png", ITEM_SIZE)
        self.door2.init_door(self.room2, self.room1, (500,500), (910, 170))

        self.key2 = Key("assets/items/key.png", ITEM_SIZE)
        self.key2.init_key(self.room2, self.door2, (400, 400), "This is the key for door2")

        # The items in room one
        self.door1 = Door("assets/items/door.png", ITEM_SIZE)
        self.door1.init_door(self.room1, self.room2, (910,170), (500, 500))

        self.key1 = Key("assets/items/key.png", ITEM_SIZE)
        self.key1.init_key(self.room1, self.door1, (400, 400), "This is the key for door1")

        # normal item
        self.item2 = Item("assets/items/key.png", ITEM_SIZE)
        self.item2.set_position(300, 300)
        self.item2.description = "This is just an item"
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

        # draw current rooms contents
        self.__draw_room(self.current_room)

        # Draw bag and player
        self._screen.blit(self.bag.bag_image, self.bag.bag_rect)
        self._screen.blit(self.bag.hover_image, self.bag.hover_rect)
        self._screen.blit(self.player.image, self.player.rect)

        self.dialog.display(self._screen, self.bag.items_list[self.bag.index])
        # self.dialog.display(self._screen)
        # x = self.player.rect.x
        # y = self.player.rect.y

        # Draw the contents inside of the bag
        for item in self.bag.bagGroup:
            self._screen.blit(item.image, item.rect)
        # Draw the contents inside of the keys group
        for item in self.bag.keysGroup:
            self._screen.blit(item.image, item.rect)

        self.player.move()

        # collide = pygame.sprite.collide_mask(
        #     self.player, self.current_room.walls)
        # if collide != None:
        #     self.player.rect.x = x
        #     self.player.rect.y = y

    def __event_handle(self):

        # all the one time press events would go here. (move is not one time press events becase
        # when you press left and don't release, the player is keeping moving left)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.__quit_game()
            if event.type == pygame.KEYDOWN:
                # press a, to select next item in the bag
                if event.key == pygame.K_a:
                    if self.bag.index > 0:
                        self.bag.hover_rect.x -= 110
                        self.bag.index -= 1
                # d to select the next prev item in the bag
                elif event.key == pygame.K_d:
                    if self.bag.index < 8:
                        self.bag.hover_rect.x += 110
                        self.bag.index += 1
                # press space, put the item selected in the bag to current room at the same location of player
                elif event.key == pygame.K_SPACE:
                    # Gets the item that the player chose (Consider Revising)
                    item = self.bag.items_list[self.bag.index]
                    if item != 0:
                        # figure out what kind of item is it, if it is a key type, then it would be set to/remove from keys group.
                        # As items getting more and more, we can encapsulate this into a function
                        if type(item) == type(Key("assets/items/key.png", size=None)):
                            bag_group = self.bag.keysGroup
                            room_group = self.current_room.keysGroup
                        elif type(item) == type(Item("assets/items/key.png", size=None)):
                            bag_group = self.bag.bagGroup
                            room_group = self.current_room.itemsGroup
                        self.bag.remove_item(item, bag_group)
                        self.current_room.addItemTo(
                            item, self.player.rect, room_group)
                elif event.key == pygame.K_1:
                    # needs to be changed
                    self.player.open_door(
                        self, self.bag.items_list[self.bag.index])
                elif event.key == pygame.K_q:
                    self.__quit_game()

    def __collide_check(self):
        # add item
        if self.bag.remain > 0:
            # if player collide with a item in items group(they are almost the same, potentially could be encapuslate into a function)
            collide = pygame.sprite.spritecollide(
                self.player, self.current_room.itemsGroup, False, pygame.sprite.collide_mask)
            # this is a list

            if collide:
                # this is to get the real item in that list(in most of the cases, this list would only have one element)
                for item in collide:
                    # remove item from current room's items group
                    item.remove(self.current_room.itemsGroup)
                    # add item to bag's item group
                    self.bag.append_item(item, self.bag.bagGroup)

            # if the player collide with a key
            collide = pygame.sprite.spritecollide(
                self.player, self.current_room.keysGroup, False, pygame.sprite.collide_mask)

            if collide:
                for item in collide:
                    item.remove(self.current_room.keysGroup)
                    self.bag.append_item(item, self.bag.keysGroup)

    def __draw_room(self, room):
        # Draw background
        self._screen.blit(room.image, room.rect)
        # Draw the necessary groups
        for item in room.itemsGroup:
            self._screen.blit(item.image, item.rect)
        for door in room.doorGroup:
            self._screen.blit(door.image, door.rect)
        for key in room.keysGroup:
            self._screen.blit(key.image, key.rect)

    # pass next room and set current_room to next room
    def switch_room(self, next_room):
        self.current_room = next_room

    def __quit_game(self):
        pygame.quit()
        exit()
