import random
import os
import random
import pygame

Field_size = 10
CELL_SIZE = 50

WIDTH = CELL_SIZE * Field_size
HEIGHT = CELL_SIZE * Field_size
BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255, 255,0)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)

class Window(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.touch_number=0
        self.touch_square=(-1,-1)
        for i in range(Field_size):
            pygame.draw.line(self.image,BLACK, (i*CELL_SIZE,0) , (i*CELL_SIZE,HEIGHT))
            pygame.draw.line(self.image,BLACK, (0,i*CELL_SIZE) ,(WIDTH ,i*CELL_SIZE))

    def fill_square(self,coords,color):
        i=coords[0]
        j=coords[1]
        pygame.draw.rect(self.image, color,
                         ((i - 1) * CELL_SIZE, (j - 1) * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def search_the_square (self, event):
        mp = event.pos
        for i in range(Field_size + 1):
            if (i * CELL_SIZE - mp[0]) // CELL_SIZE == 0:
                for j in range(Field_size + 1):
                    if (j * CELL_SIZE - mp[1]) // CELL_SIZE == 0:
                        return (i,j)

    def swap(self,coords1,coords2):
        #махнуть местами фишки
        pass

    def update (self, event=0):
        if event==0:
            return
        self.touch_number+=1

        if self.touch_number==2:
            self.touch_number=0
            #проверка, что квадратик соседний, которой еще нет....

            coords1=self.touch_square
            coords2=self.search_the_square(event)
            self.swap(coords1,coords2)

            self.fill_square(coords1,WHITE)

        else:
            self.touch_square=self.search_the_square(event)
            self.color = WHITE
            flag=(event.type == pygame.MOUSEBUTTONUP)
            if flag:
                flag=False
                self.fill_square(self.touch_square,YELLOW)

        for i in range(Field_size):
            pygame.draw.line(self.image,BLACK, (i*CELL_SIZE,0) , (i*CELL_SIZE,HEIGHT))
            pygame.draw.line(self.image,BLACK, (0,i*CELL_SIZE) ,(WIDTH ,i*CELL_SIZE))



all_sprites = pygame.sprite.Group()
s = Window()
all_sprites.add(s)





running = True
while running:
       
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if  event.type == pygame.MOUSEBUTTONUP:
            all_sprites.update(event)
    all_sprites.update()
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()
    
        
