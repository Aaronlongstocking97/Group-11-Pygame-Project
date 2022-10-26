import pygame
from GameSprites import *
from Item import Item
from Hero import Hero


class MainGame(object):

    def __init__(self):
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()

        self.hero = Hero(0,0,"assets/character/character_temp.png")

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

        # self.items_group.add(self.item)

        # This is going to create a sprite group that can store objects
        self.xxx_group = pygame.sprite.Group()

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

    def process_events(self):

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                 self.Hero.move_right()
                elif event.key == pygame.K_LEFT:
                 self.Hero.move_left()
                elif event.key == pygame.K_UP:
                 self.Hero.move_up()
                elif event.key == pygame.K_DOWN:
                 self.Hero.move_down()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                  self.Hero.stop_move_right()
                elif event.key == pygame.K_LEFT:
                  self.Hero.stop_move_left()
                elif event.key == pygame.K_UP:
                  self.Hero.stop_move_up()
                elif event.key == pygame.K_DOWN:
                  self.Hero.stop_move_down()

        return False

def main():

    start = MainGame()

    start.startGame()


if __name__ == "__main__":
    main()
