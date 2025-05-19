import pygame
import sys


screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("Puissance 4")

#pieces = pygame.image.load("")
tableau = pygame.image.load("tab p4.png")
fond = pygame.image.load("blanc.png")

fd = pygame.transform.rotozoom(fond, 0, 7.5)
tab = pygame.transform.rotozoom(tableau, 0, 0.675)
#pcs = pygame.transform.rotozoom(pieces, 0, 1.02)

screen.blit(fd, (0,0))
screen.blit(tab, (400,0))
pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()    