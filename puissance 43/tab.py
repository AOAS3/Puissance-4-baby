import pygame
import sys
from pygame.locals import *
import time
from random import randint

tour = 1
tour_j1 = 0
tour_j2 = 0
cln1_pln = 0
cln2_pln = 0
cln3_pln = 0
cln4_pln = 0
cln5_pln = 0
cln6_pln = 0
cln7_pln = 0
win_j1 = 0
win_j2 = 0
tours = tour_j1 + tour_j2

pygame.init()
screen = pygame.display.set_mode((1200,800))
pygame.display.set_caption("Puissance 4")

pc_r = pygame.image.load("jeton rouge.png")
pc_j = pygame.image.load("jeton jaune.png")
tableau = pygame.image.load("tab p4.png")
fond = pygame.image.load("blanc.png")
player1 = pygame.image.load("P1.png")
player2 = pygame.image.load("P2.png")
tourj1 = pygame.image.load("tj1.png")
tourj2 = pygame.image.load("tj2.png")
cache = pygame.image.load("cache.png")
warn = pygame.image.load("warning.png")

fd = pygame.transform.rotozoom(fond, 0, 7.5)
tab = pygame.transform.rotozoom(tableau, 0, 0.455)
pcs = pygame.transform.rotozoom(pc_r, 0, 0.485)
pcs1 = pygame.transform.rotozoom(pc_j, 0, 0.485)
p1 = pygame.transform.rotozoom(player1, 0, 0.5)
p2 = pygame.transform.rotozoom(player2, 0, 0.5)
tj1 = pygame.transform.rotozoom(tourj1, 0, 0.5)
tj2 = pygame.transform.rotozoom(tourj2, 0, 0.5)
cah = pygame.transform.rotozoom(cache, 0, 1)
wrng = pygame.transform.rotozoom(warn, 0, 0.65)

screen.blit(fd, (0,0))
screen.blit(tab, (400,60))
screen.blit(pcs, (110,150))
screen.blit(pcs1, (110, 60))
screen.blit(p1, (20,60))
screen.blit(p2, (20, 150))
screen.blit(tj1, (20,400))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP1:
                tours += 1
#_______________________________________________________________________________________________________________________________          
            #Joueur 1 joue 0 tour 1
            if tour == 1 and event.key == pygame.K_KP0 :
                screen.blit(cache, (20,400))
                screen.blit(pcs1, (503,627))
                screen.blit(tj2, (20,400))
                pygame.display.flip()
                tour = 2
                tour_j1 += 1
            elif tour == 2 and event.key == pygame.K_KP0 :
                screen.blit(cache, (20,400))
                screen.blit(pcs, (503,523))
                screen.blit(tj1, (20,400))
                pygame.display.flip()
                tour = 3
            elif tour == 3 and event.key == pygame.K_KP0 :
                screen.blit(cache, (20,400))
                screen.blit(pcs1, (503,419))
                screen.blit(tj2, (20,400))
                pygame.display.flip()
                tour = 4
            elif tour == 4 and event.key == pygame.K_KP0 :
                screen.blit(cache, (20,400))
                screen.blit(pcs, (503,314))
                screen.blit(tj1, (20,400))
                pygame.display.flip()
                tour = 5
            elif tour == 5 and event.key == pygame.K_KP0 :
                screen.blit(cache, (20,400))
                screen.blit(pcs1, (503,209))
                screen.blit(tj2, (20,400))
                pygame.display.flip()
                tour = 6
            elif tour == 6 and event.key == pygame.K_KP0 :
                screen.blit(cache, (20,400))
                screen.blit(pcs, (503,104))
                screen.blit(tj1, (20,400))
                pygame.display.flip()
                tour = 7
                cln1_pln = 1
            
            
            #Joueur 1 joue 1 au tour 1
            elif tour == 1 and event.key == pygame.K_KP1 :
                screen.blit(cache, (20,400))
                screen.blit(pcs1, (580,627))
                screen.blit(tj2, (20,400))
                pygame.display.flip()
                tour = 2
            elif tour == 2 and event.key == pygame.K_KP1 :
                screen.blit(cache, (20,400))
                screen.blit(pcs, (580,523))
                screen.blit(tj1, (20,400))
                pygame.display.flip()
                tour = 3
            elif tour == 3 and event.key == pygame.K_KP1 :
                screen.blit(cache, (20,400))
                screen.blit(pcs1, (580,419))
                screen.blit(tj2, (20,400))
                pygame.display.flip()
                tour = 4
            elif tour == 4 and event.key == pygame.K_KP1 :
                screen.blit(cache, (20,400))
                screen.blit(pcs, (580,314))
                screen.blit(tj1, (20,400))
                pygame.display.flip()
                tour = 5
            elif tour == 5 and event.key == pygame.K_KP1 :
                screen.blit(cache, (20,400))
                screen.blit(pcs1, (580,209))
                screen.blit(tj2, (20,400))
                pygame.display.flip()
                tour = 6
            elif tour == 6 and event.key == pygame.K_KP1 :
                screen.blit(cache, (20,400))
                screen.blit(pcs, (580,104))
                screen.blit(tj2, (20,400))
                pygame.display.flip()
                tour = 7
                cln2_pln = 1
                
                
            #Joueur 1 joue 2 au tour 1
            elif tour == 1 and event.key == pygame.K_KP2 :
                screen.blit(cache, (20,400))
                screen.blit(pcs1, (657,627))
                screen.blit(tj2, (20,400))
                pygame.display.flip()
                tour = 2
            elif tour == 2 and event.key == pygame.K_KP2 :
                screen.blit(cache, (20,400))
                screen.blit(pcs, (657,523))
                screen.blit(tj1, (20,400))
                pygame.display.flip()
                tour = 3
            elif tour == 3 and event.key == pygame.K_KP2 :
                screen.blit(cache, (20,400))
                screen.blit(pcs1, (657,419))
                screen.blit(tj2, (20,400))
                pygame.display.flip()
                tour = 4
            elif tour == 4 and event.key == pygame.K_KP2 :
                screen.blit(cache, (20,400))
                screen.blit(pcs, (657,314))
                screen.blit(tj1, (20,400))
                pygame.display.flip()
                tour = 5
            elif tour == 5 and event.key == pygame.K_KP2 :
                screen.blit(cache, (20,400))
                screen.blit(pcs1, (657,209))
                screen.blit(tj2, (20,400))
                pygame.display.flip()
                tour = 6
            elif tour == 6 and event.key == pygame.K_KP2 :
                screen.blit(cache, (20,400))
                screen.blit(pcs, (657,104))
                screen.blit(tj1, (20,400))
                pygame.display.flip()
                tour = 7
                cln3_pln = 1
                
                
            #Joueur 1 joue 3 au tour 1
            elif tour == 1 and event.key == pygame.K_KP3 :
                screen.blit(cache, (20,400))
                screen.blit(pcs1, (734,627))
                screen.blit(tj2, (20,400))
                pygame.display.flip()
                tour = 2
            elif tour == 2 and event.key == pygame.K_KP3 :
                screen.blit(cache, (20,400))
                screen.blit(pcs, (734,523))
                screen.blit(tj1, (20,400))
                pygame.display.flip()
                tour = 3
            elif tour == 3 and event.key == pygame.K_KP3 :
                screen.blit(cache, (20,400))
                screen.blit(pcs1, (734,419))
                screen.blit(tj2, (20,400))
                pygame.display.flip()
                tour = 4
            elif tour == 4 and event.key == pygame.K_KP3 :
                screen.blit(cache, (20,400))
                screen.blit(pcs, (734,314))
                screen.blit(tj1, (20,400))
                pygame.display.flip()
                tour = 5
            elif tour == 5 and event.key == pygame.K_KP3 :
                screen.blit(cache, (20,400))
                screen.blit(pcs1, (734,209))
                screen.blit(tj2, (20,400))
                pygame.display.flip()
                tour = 6
            elif tour == 6 and event.key == pygame.K_KP3 :
                screen.blit(cache, (20,400))
                screen.blit(pcs, (734,104))
                screen.blit(tj1, (20,400))
                pygame.display.flip()
                tour = 7
                cln4_pln = 1
                
                
            #Joueur 1 joue 4 au tour 1
            elif tour == 1 and event.key == pygame.K_KP4 :
                screen.blit(cache, (20,400))
                screen.blit(pcs1, (812,627))
                screen.blit(tj2, (20,400))
                pygame.display.flip()
                tour = 2
            elif tour == 2 and event.key == pygame.K_KP4 :
                screen.blit(cache, (20,400))
                screen.blit(pcs, (812,523))
                screen.blit(tj1, (20,400))
                pygame.display.flip()
                tour = 3
            elif tour == 3 and event.key == pygame.K_KP4 :
                screen.blit(cache, (20,400))
                screen.blit(pcs1, (812,419))
                screen.blit(tj2, (20,400))
                pygame.display.flip()
                tour = 4
            elif tour == 4 and event.key == pygame.K_KP4 :
                screen.blit(cache, (20,400))
                screen.blit(pcs, (812,314))
                screen.blit(tj1, (20,400))
                pygame.display.flip()
                tour = 5
            elif tour == 5 and event.key == pygame.K_KP4 :
                screen.blit(cache, (20,400))
                screen.blit(pcs1, (812,209))
                screen.blit(tj2, (20,400))
                pygame.display.flip()
                tour = 6
            elif tour == 1 and event.key == pygame.K_KP4 :
                screen.blit(cache, (20,400))
                screen.blit(pcs, (812,104))
                screen.blit(tj1, (20,400))
                pygame.display.flip()
                tour = 7
                cln5_pln = 1
                
                
            #Joueur 1 joue 5 au tour 1
            elif tour == 1 and event.key == pygame.K_KP5 :
                screen.blit(cache, (20,400))
                screen.blit(pcs1, (890,627))
                screen.blit(tj2, (20,400))
                pygame.display.flip()
                tour = 2
            elif tour == 2 and event.key == pygame.K_KP5 :
                screen.blit(cache, (20,400))
                screen.blit(pcs, (890,523))
                screen.blit(tj1, (20,400))
                pygame.display.flip()
                tour = 3
            elif tour == 3 and event.key == pygame.K_KP5 :
                screen.blit(cache, (20,400))
                screen.blit(pcs1, (890,419))
                screen.blit(tj2, (20,400))
                pygame.display.flip()
                tour = 4
            elif tour == 4 and event.key == pygame.K_KP5 :
                screen.blit(cache, (20,400))
                screen.blit(pcs, (890,314))
                screen.blit(tj1, (20,400))
                pygame.display.flip()
                tour = 5
            elif tour == 5 and event.key == pygame.K_KP5 :
                screen.blit(cache, (20,400))
                screen.blit(pcs1, (890,209))
                screen.blit(tj2, (20,400))
                pygame.display.flip()
                tour = 6
            elif tour == 6 and event.key == pygame.K_KP5 :
                screen.blit(cache, (20,400))
                screen.blit(pcs, (890,104))
                screen.blit(tj1, (20,400))
                pygame.display.flip()
                tour = 7
                cln6_pln = 1
                
                
            #Joueur 1 joue 6 au tour 1
            elif tour == 1 and event.key == pygame.K_KP6 :
                screen.blit(cache, (20,400))
                screen.blit(pcs1, (967,627))
                screen.blit(tj2, (20,400))
                pygame.display.flip()
                tour = 2
            elif tour == 2 and event.key == pygame.K_KP6 :
                screen.blit(cache, (20,400))
                screen.blit(pcs, (967,523))
                screen.blit(tj1, (20,400))
                pygame.display.flip()
                tour = 3
            elif tour == 3 and event.key == pygame.K_KP6 :
                screen.blit(cache, (20,400))
                screen.blit(pcs1, (967,419))
                screen.blit(tj2, (20,400))
                pygame.display.flip()
                tour = 4
            elif tour == 4 and event.key == pygame.K_KP6 :
                screen.blit(cache, (20,400))
                screen.blit(pcs, (967,314))
                screen.blit(tj1, (20,400))
                pygame.display.flip()
                tour = 5
            elif tour == 5 and event.key == pygame.K_KP6 :
                screen.blit(cache, (20,400))
                screen.blit(pcs1, (967,209))
                screen.blit(tj2, (20,400))
                pygame.display.flip()
                tour = 6
            elif tour == 6 and event.key == pygame.K_KP6 :
                screen.blit(cache, (20,400))
                screen.blit(pcs, (967,104))
                screen.blit(tj1, (20,400))
                pygame.display.flip()
                tour = 7
                cln7_pln = 1
#____________________________________________________________________________________________________________________________________________
                
            elif event.type == pygame.KEYUP and event.key == pygame.K_KP0 or event.key == pygame.K_KP1 or event.key == pygame.K_KP2 or event.key == pygame.K_KP3 or event.key == pygame.K_KP4 or event.key == pygame.K_KP5 or event.key == pygame.K_KP6:
                time.sleep(0.2) #décalage pour chgmt de tour
            elif cln1_pln == 1 or cln2_pln == 1 or cln3_pln == 1 or cln4_pln == 1 or cln5_pln == 1 or cln6_pln == 1 or cln7_pln == 1 :
                screen.blit(wrng, (80,650))
                screen.blit(wrng, (200, 650))
                pygame.display.flip()
                time.sleep(2)
                screen.blit(cache, (20, 400))
                screen.blit(cache, (20,600))
                pygame.display.flip()
                if cln1_pln == 1:
                    k = randint(2,7)
                    if k == 2 and tour%2 == 0:
                        screen.blit(cache, (20,400))
                        screen.blit(tj1, (20,400))
                        #screen.blit(pcs,)
                        pygame.display.flip()
                elif cln2_pln == 1:
                    k = randint(1,7)
                    if k == 2 :
                        k = randint(1,7)
                elif cln3_pln == 1:
                    k = randint(1,7)
                    if k == 3 :
                        k = randint(1,7)
                elif cln4_pln == 1:
                    k = randint(1,7)
                    if k == 4 :
                        k = randint(1,7)
                elif cln5_pln == 1:
                    k = randint(1,7)
                    if k == 5 :
                        k = randint(1,7)
                elif cln6_pln == 1:
                    k = randint(1,7)
                    if k == 6 :
                        k = randint(1,7)
                elif cln7_pln == 1:
                    k = randint(1,6)
            if tours == 42 :
                pygame.transform.rotozoom(fd, 0, 10)
                screen.blit(fd, (0,0))
                pygame.display.flip()
                screen.blit(tab, (400,60))
                screen.blit(pcs, (110,150))
                screen.blit(pcs1, (110, 60))
                screen.blit(p1, (20,60))
                screen.blit(p2, (20, 150))
                screen.blit(tj1, (20,400))
                pygame.display.flip()
                tours = 0
                tour = 1
                