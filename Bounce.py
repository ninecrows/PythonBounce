import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Bounce")

circlex = 400.0
circley = 300.0

deltax = 400.0
deltay = 400.0

applyx = deltax
applyy = deltay

then = pygame.time.get_ticks()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 255), (circlex, circley), 20)

    now = pygame.time.get_ticks()
    deltat: float = float(now - then)

    circlex += (applyx * (deltat / 1000.0))
    circley += (applyy * (deltat / 1000.0))

    if circlex > (800.0 - 10.0):
        applyx = -deltax
    elif circlex < 10.0:
        applyx = deltax

    if circley > (600.0 - 10.0):
        applyy = -deltay
    elif circley < 10.0:
        applyy = deltay

    then = now

    pygame.display.flip()
