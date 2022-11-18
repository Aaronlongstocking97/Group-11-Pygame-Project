from item import *


class AnswerBox(Item):

    def __init__(self, image_path, size):
        super().__init__(image_path, size)
        self.font = pygame.font.SysFont('timesnewroman', 30)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.centery = SCREEN_RECT.centery - 300
        self.input = "= "
        


    def display(self, callback):
        ouput = self.font.render(self.input, True, BLACK)
        callback._screen.blit(self.image, self.rect)
        callback._screen.blit(ouput, (self.rect.x + 20, self.rect.y + 10))



    def receive_input(self, callback, events):
        for event in events:
            if event.type ==pygame.KEYDOWN:
                if 48 <= event.key <= 58:
                    callback.math_room.answer_box.input += chr(event.key)
                elif event.key == 8 and callback.math_room.answer_box.input != "= ":
                    callback.math_room.answer_box.input = callback.math_room.answer_box.input[:-1]


    def check_answer(self, callback, evnets):

        for event in evnets:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    answer = str(callback.math_room.ans)
                    if answer == self.input[2:]:
                        return True
                    else:
                        return False