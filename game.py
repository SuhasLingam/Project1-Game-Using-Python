import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 120)

image_sky = pygame.image.load("graphics/Sky.png").convert_alpha()
image_land = pygame.image.load("graphics/ground.png").convert_alpha()
text_onscreen = test_font.render('My Game', False, 'Black')
snail_image = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_move_x = 800
snail_rect = snail_image.get_rect(midbottom=(800,300))
image_run = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
image_rect = image_run.get_rect(midbottom=(120, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.blit(image_sky, (0, 0))
    screen.blit(image_land, (0, 300))
    screen.blit(text_onscreen, (250, 50))

    snail_move_x -= 5
    if snail_move_x < -100:
        snail_move_x = 800
    screen.blit(snail_image, (snail_move_x, snail_rect))
    screen.blit(image_run, image_rect)
    pygame.display.update()
    clock.tick(60)
