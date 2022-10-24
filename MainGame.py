import pygame
from GameSprites import *
from Item import Item


class MainGame(object):

    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()

        self.__create_sprites()

    def startGame(self):

        while True:

            self.clock.tick(FRAME_RATE)
            
            self.__update_sprites()

            self.__event_handle()

            self.__collide_check()

            pygame.display.update()

    def __create_sprites(self):
        
        # This is going to create a sprite group that can store objects 
        self.items_group = pygame.sprite.Group()
        self.item = Item("player.png")
        self.item.set_size((10, 10))

    def __update_sprites(self):
        self.screen.blit(self.item.image, self.item.rect)
        # for xxx in self.xxx_group:
        #     # This is goint to draw every object in this group to the screen
        #     self.screen.blit("object.image", "object.rect")

    def __event_handle(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__quit_game()
            
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

