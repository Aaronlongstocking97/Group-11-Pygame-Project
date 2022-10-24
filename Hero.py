import pygame

class Hero(pygame.sprite.Sprite):

    change_x = 0
    change_y = 0
    game_over = False
    def __init__(self,x,y,filename):
    
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

        img = pygame.image.load("Asset/Player.png").convert() 

        # self.move_right_animation = Animation(img,32,32)
        # self.move_left_animation = Animation(pygame.transform.flip(img,True,False),32,32)
        # self.move_up_animation = Animation(pygame.transform.rotate(img,90),32,32)
        # self.move_down_animation = Animation(pygame.transform.rotate(img,270),32,32)

        self.player_image = pygame.image.load(filename).convert()
        self.player_image.set_colorkey(BLACK)

    def update(self,horizontal_blocks,vertical_blocks):

            # Character Move       

            self.rect.x += self.change_x
            self.rect.y += self.change_y

            # Collision to walls

            for block in pygame.sprite.spritecollide(self,horizontal_blocks,False):
                self.rect.centery = block.rect.centery
                self.change_y = 0
            for block in pygame.sprite.spritecollide(self,vertical_blocks,False):
                self.rect.centerx = block.rect.centerx
                self.change_x = 0

            # Change hero image by the direction hero toward

            if self.change_x > 0:
                self.move_right_animation.update(10)
                self.image = self.move_right_animation.get_current_image()
            elif self.change_x < 0:
                self.move_left_animation.update(10)
                self.image = self.move_left_animation.get_current_image()

            if self.change_y > 0:
                self.move_down_animation.update(10)
                self.image = self.move_down_animation.get_current_image()
            elif self.change_y < 0:
                self.move_up_animation.update(10)
                self.image = self.move_up_animation.get_current_image()
            
    # Hero walk speed

    def move_right(self):
        self.change_x = 3

    def move_left(self):
        self.change_x = -3

    def move_up(self):
        self.change_y = -3

    def move_down(self):
        self.change_y = 3

    def stop_move_right(self):
        if self.change_x != 0:
            self.image = self.player_image
        self.change_x = 0

    def stop_move_left(self):
        if self.change_x != 0:
            self.image = pygame.transform.flip(self.player_image,True,False)
        self.change_x = 0

    def stop_move_up(self):
        if self.change_y != 0:
            self.image = pygame.transform.rotate(self.player_image,90)
        self.change_y = 0

    def stop_move_down(self):
        if self.change_y != 0:
            self.image = pygame.transform.rotate(self.player_image,270)
        self.change_y = 0



class Animation(object):

    def __init__(self,img,width,height):

        self.sprite_sheet = img
        self.image_list = []
        self.load_images(width,height)
        self.index = 0
        self.clock = 1
        
    def load_images(self,width,height):
        for y in range(0,self.sprite_sheet.get_height(),height):
            for x in range(0,self.sprite_sheet.get_width(),width): 
                img = self.get_image(x,y,width,height)
                self.image_list.append(img)

    def get_image(self,x,y,width,height):
        image = pygame.Surface([width,height]).convert()
        image.blit(self.sprite_sheet,(0,0),(x,y,width,height))
        image.set_colorkey((0,0,0))
        return image

    def get_current_image(self):
        return self.image_list[self.index]

    def get_length(self):
        return len(self.image_list)

    def update(self,fps=30):
        step = 30 // fps
        if self.clock == 30:
            self.clock = 1
        else:
            self.clock += 1

        if self.clock in range(1,30,step):
            self.index += 1
            if self.index == len(self.image_list):
                self.index = 0