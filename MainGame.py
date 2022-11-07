import pygame
from GameSprites import *
from item import Item
from Player import Player
from bag import *
from item import Item
from background import *


class MainGame(object):

    pygame.init()

    def __init__(self):
        self._screen = pygame.display.set_mode(SCREEN_RECT.size)
        self._clock = pygame.time.Clock()

        self.__create_sprites()

        self.room1Display = True

    def startGame(self):

        while True:

            self._clock.tick(FRAME_RATE)

            self.__update_sprites()

            self.__event_handle()

            self.__collide_check()

            pygame.display.update()

    def __create_sprites(self):

        self.bag_group = pygame.sprite.Group()
        self.bag = Bag()
        self.player = Player("player.png")

        self.room1 = RoomOne()
        self.room1.createRoomOne()
        

    def __update_sprites(self):
        if self.room1Display:
            self.room1.DrawRoomOne(self)
        

        self._screen.blit(self.bag.bag_image, self.bag.bag_rect)
        self._screen.blit(self.bag.hover_image, self.bag.hover_rect)
        self._screen.blit(self.player.image, self.player.rect)
        for item in self.bag.items_list:
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


    def __collide_check(self):
        if pygame.sprite.collide_mask(self.player, self.room1.item):
        # test = pygame.sprite.spritecollide(self.player, self.items_group, True, pygame.sprite.collide_mask)
            self.bag.append_item(self.room1.item)
            self.room1.removeItemFrom(self.room1.item)

        if pygame.sprite.collide_mask(self.player, self.room1.item2):
        # test = pygame.sprite.spritecollide(self.player, self.items_group, True, pygame.sprite.collide_mask)
            self.bag.append_item(self.room1.item2)
            self.room1.removeItemFrom(self.room1.item2)

    def __quit_game(self):
        pygame.quit()
        exit()


def main():

    start = MainGame()

    start.startGame()


if __name__ == "__main__":
    main()
