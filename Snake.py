import pygame, random

from pygame.math import Vector2


class FRUIT:
    def __init__(self):
        self.x = random.randint(0,cell_number - 1)
        self.y = random.randint(0,cell_number - 1)
        self.pos = Vector2(self.x,self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size),cell_size,cell_size)
        pygame.draw.rect(screen,(206,0,0),fruit_rect)


pygame.init()

cell_size = 30
cell_number = 20

screen = pygame.display.set_mode((cell_number*cell_size, cell_number*cell_size))

clock = pygame.time.Clock()

fruit = FRUIT()

player = pygame.Rect((300,250,25,25))


run = True

while run:

    screen.fill((0,0,0))

    fruit.draw_fruit()

    pygame.draw.rect(screen, (255,0,0), player)

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-5,0)
    elif key[pygame.K_d] == True:
        player.move_ip(5,0)
    elif key[pygame.K_w] == True:
        player.move_ip(0,-5)
    elif key[pygame.K_s] == True:
        player.move_ip(0,5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(60)


pygame.quit()