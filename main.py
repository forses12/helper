



import pygame

a = pygame.image.load('images/flower1.png')
pygame.draw.circle(a, [255, 0, 0], [50, 330], 40)
# pygame.image.save(a, 'images/bbbb1.png')


r = pygame.Surface([300, 500])
r.fill([255, 255, 255])
pygame.draw.rect(r, [255, 0, 0], [10, 10, 200, 200])
pygame.draw.line(r, [255, 0, 0], [10, 220], [200, 270], 3)
pygame.draw.aaline(r, [255, 0, 0], [10, 230], [200, 280])
pygame.draw.circle(r, [255, 0, 0], [50, 330], 40)
pygame.image.save(r, 'images/bbbb.png')

screen = pygame.display.set_mode([400, 600])


d=pygame.Surface([700,700])
d.blit(a,(50,100))
d.blit(a,(150,200))

pygame.image.save(d,'images/ddd3.png')
