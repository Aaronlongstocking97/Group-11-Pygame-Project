from GameSprites import *


class Dialog():

    def __init__(self):
        self.font = pygame.font.SysFont('timesnewroman', 30)
        # self.window = pygame.display.set_mode((500, 500))
        # self.clock = pygame.time()

    def display(self, screen):

        # popUp = True
        # while popUp:
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             pygame.quit()
        #             quit()
        #         if event.type == pygame.KEYDOWN:
        #             if event.key == pygame.K_c:
        #                 popUp = False

        #             elif event.key == pygame.K_q:
        #                 pygame.quit()
        #                 quit()

        sampleText = "This works its amazing"
        img = self.font.render(sampleText, True, BLACK, WHITE)
        # rect = img.get_rect()
        # pygame.draw.rect(img, WHITE, rect)
        # pygame.Surface.fill(screen, WHITE, rect, 1)
        screen.blit(img, (20, 20))
        pygame.display.update()
        # self.clock.tick(5)
