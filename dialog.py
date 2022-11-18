from GameSprites import *


class Dialog():

    def __init__(self):
        self.font = pygame.font.SysFont('timesnewroman', 30)

    def display(self, screen, item):

        if item != 0:
            sampleText = item.description
        else:
            sampleText = " "

        img = self.font.render(sampleText, True, BLACK, WHITE)
        screen.blit(img, (20, 20))

