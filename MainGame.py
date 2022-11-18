import pygame
from GameSprites import *
from item import *
from Player import *
from bag import *
from scene import *
from door import *
from dialog import *
from key import *
from mathroom import *
from hallway import *

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
        self.current_room = self.hallway

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

        # create rooms
        self.math_room = MathRoom(MATH_ROOM)
        self.hallway = Hallway(HALLWAY)

        # initialize rooms
        self.math_room.init_math_room(self)
        self.hallway.init_hallway(self)

        self.dialog = Dialog()


    def __update_sprites(self):

        # draw current rooms contents
        self.__draw_room(self.current_room)

        # Draw bag and player
        self._screen.blit(self.bag.bag_image, self.bag.bag_rect)
        self._screen.blit(self.bag.hover_image, self.bag.hover_rect)
        self._screen.blit(self.player.image, self.player.rect)

        self.dialog.display(self._screen, self.bag.items_list[self.bag.index])

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
                    self.bag.move_hover_left()

                # d to select the next prev item in the bag
                elif event.key == pygame.K_d:
                    self.bag.move_hover_right()

                # press space, put the item selected in the bag to current room at the same location of player
                elif event.key == pygame.K_SPACE:
                    self.bag.put_from_bag_event(self)

        # when player collide with a door in door group
        collide = pygame.sprite.spritecollide(
            self.player, self.current_room.doorGroup, False, pygame.sprite.collide_mask)
        if collide:
            for door in collide:
                door.show_tip(self)
                for event in events:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                        # needs to be changed
                            self.player.open_door(
                                self, self.bag.items_list[self.bag.index], door)

        # show the pop up box for math room
        if  670 <= self.player.rect.x <= 700:
            if self.current_room == self.math_room:
                self.math_room.answer_box.display(self)
                self.math_room.answer_box.receive_input(self, events)
                player_try = self.math_room.answer_box.check_answer(self, events)
                if player_try == True:
                    print("Good Job")
                    self.math_room.reset_question()
                elif player_try == False:
                    print("傻逼")


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

        if self.current_room == self.math_room:
            self.math_room.display_question(self)


    # pass next room and set current_room to next room
    def switch_room(self, next_room):
        self.current_room = next_room


    def __quit_game(self):
        pygame.quit()
        exit()
