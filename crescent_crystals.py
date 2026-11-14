import pygame

pygame.init()

screen = pygame.display.set_mode((900, 750))
pygame.display.set_caption("my game")

clock = pygame.time.Clock()
running = True
fullscreen = False
while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    else:  
                        screen = pygame.display.set_mode((800, 600))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()