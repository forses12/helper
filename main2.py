import pygame

screen=pygame.display.set_mode([600,600])
while True:
    pygame.event.get()
    a=pygame.image.load('images/water_drop.png')
    pygame.draw.rect(screen,[56,34,75],[10,10,50,50])
    screen.blit(a,[100,100])
    pygame.display.flip()
