import pygame
from GameSprites import *
from item import Item
from Player import Player
from bag import *
from item import Item


class MainGame(object):

    pygame.init()

    def __init__(self):
        self._screen = pygame.display.set_mode(SCREEN_RECT.size)
        self._clock = pygame.time.Clock()

        self.__create_sprites()

    def startGame(self):

        while True:

            self._clock.tick(FRAME_RATE)

            self.__update_sprites()

            self.__event_handle()

            self.__collide_check()

            pygame.display.update()

    def __create_sprites(self):
        self.bag_group = pygame.sprite.Group()
        # This is going to create a sprite group that can store objects
        # self.xxx_group = pygame.sprite.Group()
        self.bag = Bag()

    def __update_sprites(self):
        self._screen.blit(self.bag.bag_image, self.bag.bag_rect)
        self._screen.blit(self.bag.hover_image, self.bag.hover_rect)

        # for xxx in self.xxx_group:
        # This is goint to draw every object in this group to the screen
        #    self.screen.blit("object.image", "object.rect")
        self.items_group = pygame.sprite.Group()
        self.item = Item("assets/items/key.png")
        self.player = Player("player.png")

        self.item.set_size((100, 100))
        self.player.set_position(50, 100)

        # This is going to create a sprite group that can store objects
        self.xxx_group = pygame.sprite.Group()

    def __update_sprites(self):
        self.screen.blit(self.item.image, self.item.rect)
        self.screen.blit(self.player.image, self.player.rect)
        self.player.move()
        
        # for xxx in self.xxx_group:
        #     # This is goint to draw every object in this group to the screen
        #     self.screen.blit("object.image", "object.rect")

    def __event_handle(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    if self.bag.index > 0:
                        self.bag.hover_rect.x -= 50
                        self.bag.index -= 1
                elif event.key == pygame.K_d:
                    if self.bag.index < 99:
                        self.bag.hover_rect.x += 50
                        self.bag.index += 1

        # This is going to add a object in this group
        # self.xxx_group.add("object")

    def __collide_check(self):
        pass

    def __quit_game(self):
        pygame.quit()
        exit()


def main():

    start = MainGame()

    start.startGame()


if __name__ == "__main__":
    main()
