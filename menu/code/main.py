import pygame
import sys
import typew2
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

#Boucle du jeu
running = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
        
