from item import *


class AnswerBox(Item):

    def __init__(self, image_path, size):
        super().__init__(image_path, size)
        self.font = pygame.font.SysFont('timesnewroman', 30)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.centery = SCREEN_RECT.centery - 300
        self.input = "= "
        self.can_write = False
        self.tip = ""
        self.active = False

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def init_answer_box(self, room, position):
        x, y = position
        self.set_position(x, y)

    def display(self, callback):
        ouput = self.font.render(self.input, True, BLACK)
        callback._screen.blit(self.image, self.rect)
        callback._screen.blit(ouput, (self.rect.x + 20, self.rect.y + 10))

    def receive_input(self, events, room):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if 48 <= event.key <= 58:
                    room.answer_box.input += chr(event.key)
                elif event.key == 8 and room.answer_box.input != "= ":
                    room.answer_box.input = room.answer_box.input[:-1]

    def check_answer(self, events, room):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    answer = str(room.ans)
                    if answer == self.input[2:]:
                        self.input = "= "
                        return True
                    else:
                        self.input = "= "
                        return False

    def show_tip(self, callback):
        return super().show_tip(callback)

    def set_tip(self, tip):
        return super().set_tip(tip)
