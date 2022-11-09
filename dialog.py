# import pygame module in this program
from pygame.locals import *
import time
from GameSprites import *


BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)


class Dialog(GameSprite):

    def __init__(self):
        super().__init__()
        # self.image = ""
        # setting the pygame font style(1st parameter)
        # and size of font(2nd parameter)
        self.font = pygame.font.SysFont('timesnewroman', 30)
        self.window = pygame.display.set_mode((500, 500))
        self.t0 = time.time()

        def display(self):

            print('time needed for Font creation :', time.time() - self.t0)

            font = pygame.font.SysFont('timesnewroman', 30)
            img = font.render('timesnewroman', True, BLUE)
            rect = img.get_rect()
            pygame.draw.rect(img, BLUE, rect, 1)
            fonts = pygame.font.get_fonts()
            print(len(fonts))
            for i in range(7):
                print(fonts[i])

            running = True
            background = GRAY
            while running:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        running = False

                self.window.fill(background)
                self.window.blit(img, (20, 20))
                pygame.display.update()

# font1 = pygame.font.SysFont('chalkduster.ttf', 72)
# img1 = font1.render('chalkduster.ttf', True, BLUE)

# font2 = pygame.font.SysFont('didot.ttc', 72)
# img2 = font2.render('didot.ttc', True, GREEN)

# fonts = pygame.font.get_fonts()
# print(len(fonts))
# for i in range(7):
#     print(fonts[i])

# running = True
# background = GRAY
# while running:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             running = False

#     self.window.fill(background)
#     self.window..blit(img, (20, 20))
#     self.window..blit(img1, (20, 50))
#     self.window..blit(img2, (20, 120))
#     pygame.display.update()

# pygame.quit()
