import pygame, random
from pygame import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(6,10), Vector2(7,10)]       # Snake's body is three blocks long
        self.screen = screen
    
    def draw_snake(self):                                               # Every vector becomes a white block on the grid
        for block in self.body:
            block_x = int(block.x * cell_size)
            block_y = int(block.y * cell_size)
            rect = pygame.Rect(block_x, block_y, cell_size, cell_size)
            pygame.draw.rect(screen, (250, 250, 250), rect)

class FRUIT:                                                            # The fruit has a random position on the grid
    def __init__(self):
        self.x = random.randint(0,cell_number - 1)
        self.y = random.randint(0,cell_number - 1)
        self.pos = Vector2(self.x,self.y)

    def draw_fruit(self):                                              # The fruit becomes a red block on the grid
        fruit_x = int(self.pos.x * cell_size)
        fruit_y = int(self.pos.y * cell_size)
        fruit_rect = pygame.Rect(fruit_x, fruit_y, cell_size, cell_size)
        pygame.draw.rect(screen,(206,0,0),fruit_rect)

pygame.init()

cell_size = 30
cell_number = 20

screen = pygame.display.set_mode((cell_number*cell_size, cell_number*cell_size))

clock = pygame.time.Clock()

fruit = FRUIT()

snake = SNAKE()


run = True

while run:

    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    snake.draw_snake()
    fruit.draw_fruit()
    pygame.display.update()
    clock.tick(60)                          # Limits the game to 60 frames per second


pygame.quit()