import pygame, random

pygame.init()

cell_size = 30
cell_number = 20



screen = pygame.display.set_mode((cell_number*cell_size, cell_number*cell_size))

clock = pygame.time.Clock()

player = pygame.Rect((300,250,25,25))


run = True

while run:

    screen.fill((0,0,0))

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