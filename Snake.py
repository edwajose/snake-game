import pygame, random
from pygame import Vector2

<<<<<<< HEAD
class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(6,10), Vector2(7,10)]   # Snake's body is three blocks long
        self.screen = screen
    
    def draw_snake(self):
        for block in self.body:
            block_x = int(block.x * cell_size)
            block_y = int(block.y * cell_size)
            rect = pygame.Rect(block_x, block_y, cell_size, cell_size)
            pygame.draw.rect(screen, (250, 250, 250), rect)
            
=======
from pygame.math import Vector2


class FRUIT:
    def __init__(self):
        self.x = random.randint(0,cell_number - 1)
        self.y = random.randint(0,cell_number - 1)
        self.pos = Vector2(self.x,self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size),cell_size,cell_size)
        pygame.draw.rect(screen,(206,0,0),fruit_rect)


>>>>>>> 56c760e6953f072df83b1c18b004fc039e07a227
pygame.init()

cell_size = 30
cell_number = 20

screen = pygame.display.set_mode((cell_number*cell_size, cell_number*cell_size))

clock = pygame.time.Clock()

fruit = FRUIT()

player = pygame.Rect((300,250,25,25))

snake = SNAKE()


run = True

while run:

    screen.fill((0,0,0))

<<<<<<< HEAD
=======
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

>>>>>>> 56c760e6953f072df83b1c18b004fc039e07a227
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    snake.draw_snake()
    pygame.display.update()
    clock.tick(60)


pygame.quit()