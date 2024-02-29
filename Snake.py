import pygame, random, sys
from pygame import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(7,10), Vector2(6,10), Vector2(5,10)]       # Snake's body is three blocks long
        self.direction = Vector2(1,0)
        self.new_block = False
    
    def draw_snake(self):                                               # Every vector becomes a white block on the grid
        for block in self.body:
            block_x = int(block.x * cell_size)
            block_y = int(block.y * cell_size)
            rect = pygame.Rect(block_x, block_y, cell_size, cell_size)
            pygame.draw.rect(screen, (250, 250, 250), rect)
    
    def move_snake(self):                                               # Make the snake move
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
    
    def lengthen(self):
        self.new_block = True


class FRUIT:                                                            # The fruit has a random position on the grid
    def __init__(self):
        self.randomize()

    def draw_fruit(self):                                              # The fruit becomes a red block on the grid
        fruit_x = int(self.pos.x * cell_size)
        fruit_y = int(self.pos.y * cell_size)
        fruit_rect = pygame.Rect(fruit_x, fruit_y, cell_size, cell_size)
        pygame.draw.rect(screen,(206,0,0),fruit_rect)
    
    def randomize(self):
        self.x = random.randint(0,cell_number - 1)
        self.y = random.randint(0,cell_number - 1)
        self.pos = Vector2(self.x,self.y)

class MAIN:                                                            # Contains the main game logic
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
    
    def update(self):
        self.snake.move_snake()
        self.eat_check()
        self.death_check()
    
    def draw_objects(self):
        self.snake.draw_snake()
        self.fruit.draw_fruit()
    
    def eat_check(self):
        if self.fruit.pos == self.snake.body[0]:
            # Eat the fruit and lengthen the snake
            self.fruit.randomize()
            self.snake.lengthen()
        for block in self.snake.body:
            if self.fruit.pos == block:
                self.fruit.randomize()
    
    def death_check(self):
        # Check if the snake is outside the screen or hitting itself
        if self.snake.body[0].x < 0 or self.snake.body[0].x >= cell_number:
            self.game_over()
        if self.snake.body[0].y < 0 or self.snake.body[0].y >= cell_number:
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
    
    def game_over(self):
        pygame.quit()
        sys.exit()

    def draw_score(self):
        score_text = "sample pause"
        score_surface = game_font.render(score_text,True,(0,0,0))
        score_x = int(cell_size*cell_number - 80)
        score_y = int(cell_size*cell_number - 80)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        screen.blit(score_surface, score_rect)
        

pygame.init()

cell_size = 30
cell_number = 20

screen = pygame.display.set_mode((cell_number*cell_size, cell_number*cell_size))

clock = pygame.time.Clock()

main_game = MAIN()

game_font = pygame.font.SysFont("Arial", 25)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)


pause = False

while True:

    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)
            if event.key == pygame.K_p:
                pause = True
                screen.fill((0,200,0))
                main_game.draw_score()
                pygame.display.update()

    while pause:
        
        

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = False

        clock.tick(60) 


    main_game.draw_objects()
    pygame.display.update()
    clock.tick(60)                          # Limits the game to 60 frames per second

