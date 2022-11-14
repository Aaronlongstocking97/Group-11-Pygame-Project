from GameSprites import *
 
class Dialog(GameSprite):
 
 def __init__(self):
    self.font = pygame.font.SysFont('timesnewroman', 30)
    # self.clock = pygame.time()
    
 def display(self, screen):
 
    sampleText = "This works its amazing"
    img = self.font.render(sampleText, True, BLACK, WHITE)
    screen.blit(img, (20, 20))
    pygame.display.update()
    # self.clock.tick(5)