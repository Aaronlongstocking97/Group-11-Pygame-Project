import pygame
import time

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
from library import *
from pen import *
from scienceroom import *
from button import *
from server import *

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
        self._startTime = 0
        self._endTime = 0
        self.server = Server()

        # This is a pointer to point the current room the player is in.
        self.current_room = None

    def startGame(self):
        # Set the current room to the first room in the game.
        self.current_room = self.hallway
        pygame.mixer.music.load(MUSIC)
        pygame.mixer.music.play(-1)

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
        self.player = Player(PLAYER_IMAGE, PLAYER_SIZE)

        # create rooms
        self.math_room = MathRoom(MATH_ROOM)
        self.hallway = Hallway(HALLWAY)
        self.library = Library(LIBRARY)
        self.science_room = ScienceRoom(SCIENCE_ROOM)
        self.winning_scene = Scene(WINNING_SCENE)

        self.math_room.create_room(self)
        self.hallway.creat_hallway(self)
        self.library.create_library(self)
        self.science_room.create_science_room(self)

        # initialize rooms
        self.math_room.init_math_room(self)
        self.hallway.init_hallway(self)
        self.library.init_library(self)
        self.science_room.init_science_room(self)

        # Initialize the dialog
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
        for item in self.bag.pensGroup:
            self._screen.blit(item.image, item.rect)

        x = self.player.rect.x
        y = self.player.rect.y

        self.player.move()

        # walls
        if self.current_room != self.winning_scene:
            collide = pygame.sprite.collide_mask(
                self.player.body, self.current_room.walls)
            if collide != None:
                self.player.set_position(x, y)

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
            self.player.body, self.current_room.doorGroup, False, pygame.sprite.collide_mask)
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
        if 430 <= self.player.body.rect.x <= 500 and 130 <= self.player.body.rect.y <= 170:
            if self.current_room == self.math_room:
                self.math_room.answer_box.display(self)
                self.math_room.answer_box.show_tip(self)
                # if you can write on the box (You have used a key)
                if self.math_room.answer_box.can_write == True:

                    self.math_room.answer_box.receive_input(events, self.math_room)
                    player_try = self.math_room.answer_box.check_answer(events, self.math_room)

                    if player_try == True:
                        self.math_room.loadingLight1.right_answer()
                        self.math_room.reset_question()
                        self.math_room.answers += 1
                    elif player_try == False:
                        self.math_room.loadingLight1.wrong_answer()
                else:
                    self.math_room.answer_box.set_tip("you need a pencil")
                    if type(self.bag.items_list[self.bag.index]) == type(Pen((PENCIL_IMAGE), size=None)):
                        for event in events:
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_q:
                                    self.math_room.answer_box.can_write = True
                                    self.bag.remove_item(self.bag.items_list[self.bag.index], self.bag.pensGroup)
                                    self.math_room.answer_box.set_tip("now you can wirte")


            if self.current_room == self.science_room:
                self.science_room.answer_box.display(self)
                self.science_room.answer_box.show_tip(self)
                self.science_room.answer_box.can_write == True
                self.science_room.answer_box.receive_input(events, self.science_room)
                player_try = self.science_room.answer_box.check_answer(events, self.science_room)
                if player_try == True:
                    self.science_room.loadingLight1.right_answer()
                    self.science_room.reset_question()
                    self.science_room.answers += 1
                elif player_try == False:
                    self.science_room.loadingLight1.wrong_answer()
               

    def __collide_check(self):
        # add item
        if self.bag.remain > 0:
            # if player collide with a item in items group(they are almost the same, potentially could be encapuslate into a function)
            collide = pygame.sprite.spritecollide(
                self.player.body, self.current_room.itemsGroup, False, pygame.sprite.collide_mask)
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
                self.player.body, self.current_room.keysGroup, False, pygame.sprite.collide_mask)

            if collide:
                for item in collide:
                    item.remove(self.current_room.keysGroup)
                    self.bag.append_item(item, self.bag.keysGroup)

            collide = pygame.sprite.spritecollide(
                self.player.body, self.current_room.pensGroup, False, pygame.sprite.collide_mask)

            if collide:
                for item in collide:
                    item.remove(self.current_room.pensGroup)
                    self.bag.append_item(item, self.bag.pensGroup)

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
        for pencil in room.pensGroup:
            self. _screen.blit(pencil.image, pencil.rect)

        if self.current_room == self.math_room:
            self.math_room.display_question(self)
            for light in room.lightsGroup:
                self._screen.blit(light.image, light.rect)
            if self.math_room.answers >= 5 and self.math_room.passed == False:
                self.math_room.pass_room(self)
                self.math_room.passed = True

        if self.current_room == self.science_room:
            self.science_room.display_question(self)
            for light in room.lightsGroup:
                self._screen.blit(light.image, light.rect)
            if self.science_room.answers >= 5 and self.science_room.passed == False:
                self.science_room.pass_room(self)
                self.science_room.passed = True

    # pass next room and set current_room to next room
    def switch_room(self, next_room):
        self.current_room = next_room

    def __quit_game(self):
        pygame.quit()
        exit()

    def get_font(size):
        return pygame.font.Font('assets/menu/font.ttf', size)

    def main_menu(self):
        while True:
            self._screen.blit(pygame.image.load("assets/menu/menuBackground.jpeg"),(0,0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = pygame.font.Font('assets/menu/font.ttf', 75).render("ESCAPE ROOM", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(500, 150))

            PLAY_BUTTON = Button(image=pygame.image.load("assets/menu/MenuRect.png"), pos=(500, 300), 
                            text_input="PLAY", font=pygame.font.Font('assets/menu/font.ttf', 50), base_color="#d7fcd4", hovering_color="White")
            RANKING_BUTTON = Button(image=pygame.image.load("assets/menu/MenuRect.png"), pos=(500, 450), 
                            text_input="RANKING", font=pygame.font.Font('assets/menu/font.ttf', 50), base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = Button(image=pygame.image.load("assets/menu/MenuRect.png"), pos=(500, 600), 
                            text_input="QUIT", font=pygame.font.Font('assets/menu/font.ttf', 50), base_color="#d7fcd4", hovering_color="White")

            self._screen.blit(MENU_TEXT, MENU_RECT)

            font = pygame.font.SysFont(None, 36)
            inst1 = "button instruction:"
            inst2 = "arrow button: move"
            inst3 = "a: select left side item"
            inst4 = "d: select right side item"
            inst5 = "q: use selected item and open a door"
            inst6 = "f: submit an answer"

            img1 = font.render(inst1, True, WHITE)
            self._screen.blit(img1, (100, 550))
            img2 = font.render(inst2, True, WHITE)
            self._screen.blit(img2, (100, 590))
            img3 = font.render(inst3, True, WHITE)
            self._screen.blit(img3, (100, 630))
            img4 = font.render(inst4, True, WHITE)
            self._screen.blit(img4, (100, 670))
            img5 = font.render(inst5, True, WHITE)
            self._screen.blit(img5, (100, 710))
            img6 = font.render(inst6, True, WHITE)
            self._screen.blit(img6, (100, 750))

            for button in [PLAY_BUTTON, RANKING_BUTTON,  QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self._screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__quit_game()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self._startTime = time.perf_counter()
                        self.startGame()
                    if RANKING_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.ranking()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.__quit_game()

            pygame.display.update()

    def end_menu(self):
        self._endTime = time.perf_counter()
        Server.postScore(self.server,self._startTime, self._endTime)

        while True:
            self._screen.blit(pygame.image.load("assets/menu/MenuBackground.png"),(0,0))
            self._screen.blit(pygame.image.load("assets/menu/image000000.png"),(0,0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = pygame.font.Font('assets/menu/font.ttf', 75).render("GOOD JOB!", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(500, 150))

            PLAY_BUTTON = Button(image=pygame.image.load("assets/menu/MenuRect.png"), pos=(500, 300), 
                            text_input="PLAY AGAIN", font=pygame.font.Font('assets/menu/font.ttf', 50), base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = Button(image=pygame.image.load("assets/menu/MenuRect.png"), pos=(500, 450), 
                            text_input="QUIT", font=pygame.font.Font('assets/menu/font.ttf', 50), base_color="#d7fcd4", hovering_color="White")

            self._screen.blit(MENU_TEXT, MENU_RECT)

            font = pygame.font.SysFont(None, 36)
            inst1 = "button instruction:"
            inst2 = "arrow button: move"
            inst3 = "a: select left side item"
            inst4 = "d: select right side item"
            inst5 = "q: use selected item and open a door"
            inst6 = "f: submit an answer"

            img1 = font.render(inst1, True, WHITE)
            self._screen.blit(img1, (100, 550))
            img2 = font.render(inst2, True, WHITE)
            self._screen.blit(img2, (100, 590))
            img3 = font.render(inst3, True, WHITE)
            self._screen.blit(img3, (100, 630))
            img4 = font.render(inst4, True, WHITE)
            self._screen.blit(img4, (100, 670))
            img5 = font.render(inst5, True, WHITE)
            self._screen.blit(img5, (100, 710))
            img6 = font.render(inst6, True, WHITE)
            self._screen.blit(img6, (100, 750))

            for button in [PLAY_BUTTON,  QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self._screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__quit_game()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.restart()
                        self.startGame()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.__quit_game()

            pygame.display.update()

    def restart(self):

        self.math_room.kill()
        self.hallway.kill()
        self.library.kill()
        self.science_room.kill()
        self.__create_sprites()

    def ranking(self):
        while True:
            self._screen.blit(pygame.image.load("assets/menu/menuBackground.jpeg"),(0,0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = pygame.font.Font('assets/menu/font.ttf', 75).render("RANKING", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(500, 150))


            BACK_BUTTON = Button(image=pygame.image.load("assets/menu/MenuRect.png"), pos=(500, 700), 
                            text_input="QUIT", font=pygame.font.Font('assets/menu/font.ttf', 50), base_color="#d7fcd4", hovering_color="White")

            self._screen.blit(MENU_TEXT, MENU_RECT)

            font = pygame.font.SysFont(None, 72)

            ranking_data = Server.getScore(self.server)
            # print(ranking_data)
            first = ("1st: "+str(ranking_data[0]))
            second = ("2nd: "+str(ranking_data[1]))
            third = ("3rd: "+str(ranking_data[2]))

            first_img = font.render(first, True, WHITE)
            self._screen.blit(first_img, (400, 200))
            second_img = font.render(second, True, WHITE)
            self._screen.blit(second_img, (400, 344))
            third_img = font.render(third, True, WHITE)
            self._screen.blit(third_img, (400, 488))

            
            

            for button in [BACK_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self._screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__quit_game()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.main_menu()

            pygame.display.update()
