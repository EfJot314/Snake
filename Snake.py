import pygame, sys
import numpy as np
import random
from pygame.locals import *




rozmiar = 700
bok = 20

pygame.init()
plansza = pygame.display.set_mode((rozmiar, rozmiar))
pygame.display.set_caption('Snake')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (129, 187, 129)
GRAY = (225, 225, 225)
RED = (255, 0, 0)
BETTER_GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)



FPS = 100
fpsClock = pygame.time.Clock()

def teren():
    plansza.fill(BLUE)
    pygame.draw.rect(plansza, BLACK,(0, 0, bok, rozmiar))
    pygame.draw.rect(plansza, BLACK,(rozmiar-bok, 0, bok, rozmiar))
    pygame.draw.rect(plansza, BLACK,(0, 0, rozmiar, bok))
    pygame.draw.rect(plansza, BLACK,(0, rozmiar-bok, rozmiar, bok))
    for i in range(int((rozmiar-2*bok)/bok)+1):
        pygame.draw.line(plansza, WHITE, (bok*(i+1), bok), (bok*(i+1), rozmiar-bok), 1)
        pygame.draw.line(plansza, WHITE, (bok, bok*(i+1)), (rozmiar-bok, bok*(i+1)), 1)



def start():
    font = pygame.font.SysFont("monospace", 30)
    l_name = font.render("SNAKE", 1, BLACK)
    l_sp = font.render("1 - Singleplayer", 1, BLACK)
    l_mp = font.render("2 - Multiplayer", 1, BLACK)
    l_exit = font.render("3 - Wyjdź", 1, BLACK)
    while True:
        plansza.fill(BETTER_GREEN)
        

        plansza.blit(l_name, (int(rozmiar/2 - 60), int(rozmiar/5)))
        plansza.blit(l_sp, (int(rozmiar/2 - 200), int(2* rozmiar/3)))
        plansza.blit(l_mp, (int(rozmiar/2 - 200), int(2* rozmiar/3)+50))
        plansza.blit(l_exit, (int(rozmiar/2 - 200), int(2* rozmiar/3)+100))
        

        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    main()
                if event.key == pygame.K_2:
                    multi()
                if event.key == pygame.K_3:
                    pygame.quit()
                    sys.exit()
            
        pygame.display.update()
        fpsClock.tick(FPS)





def koniec(dlugosc):
    font = pygame.font.SysFont("monospace", 30)
    l_end = font.render("KONIEC GRY", 1, BLACK)
    l_score = font.render(("Osiągnięta długość: "+ str(dlugosc)), 1, BLACK)
    l_newgame = font.render("1 - Nowa gra", 1, BLACK)
    l_exit = font.render("2 - Wyjdź", 1, BLACK)
    while True:
        plansza.fill(BETTER_GREEN)
        
        plansza.blit(l_end, (int(rozmiar/2 - 100), int(rozmiar/5-50)))
        plansza.blit(l_score, (int(rozmiar/2 - 200), int(rozmiar/5)))
        plansza.blit(l_newgame, (int(rozmiar/2 - 100), int(2* rozmiar/3)))
        plansza.blit(l_exit, (int(rozmiar/2 - 100), int(2* rozmiar/3)+50))
        

        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    start()
                if event.key == pygame.K_2:
                    pygame.quit()
                    sys.exit()
            
        pygame.display.update()
        fpsClock.tick(FPS)

def koniec2(dlugosc, dlugosc2, przegrana, przegrana2):
    font = pygame.font.SysFont("monospace", 30)
    l_end = font.render("KONIEC GRY", 1, BLACK)
    if przegrana == True and przegrana2 == True:
        l_who = font.render("Remis (zderzenie głowami)", 1, BLACK)
    elif przegrana == True:
        l_who = font.render("Przegrał gracz 1", 1, BLACK)
    else:
        l_who = font.render("Przegrał gracz 2", 1, BLACK)
        
    l_score1 = font.render(("Osiągnięta długość 1: "+ str(dlugosc)), 1, BLACK)
    l_score2 = font.render(("Osiągnięta długość 2: "+ str(dlugosc2)), 1, BLACK)
    l_newgame = font.render("1 - Nowa gra", 1, BLACK)
    l_exit = font.render("2 - Wyjdź", 1, BLACK)
    while True:
        plansza.fill(BETTER_GREEN)
        
        plansza.blit(l_end, (int(rozmiar/2 - 100), int(rozmiar/5-50)))
        plansza.blit(l_who, (int(rozmiar/2 - 200), int(rozmiar/5)))
        plansza.blit(l_score1, (int(rozmiar/2 - 200), int(rozmiar/5)+50))
        plansza.blit(l_score2, (int(rozmiar/2 - 200), int(rozmiar/5)+100))
        plansza.blit(l_newgame, (int(rozmiar/2 - 100), int(2* rozmiar/3)))
        plansza.blit(l_exit, (int(rozmiar/2 - 100), int(2* rozmiar/3)+50))
        

        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    start()
                if event.key == pygame.K_2:
                    pygame.quit()
                    sys.exit()
            
        pygame.display.update()
        fpsClock.tick(FPS)


def pauza(dlugosc):
    powrot = False
    font = pygame.font.SysFont("monospace", 30)
    l_end = font.render("PAUZA", 1, BLACK)
    l_score = font.render(("Osiągnięta długość: "+ str(dlugosc)), 1, BLACK)
    l_newgame = font.render("1 - Wróć do gry", 1, BLACK)
    l_exit = font.render("2 - Wyjdź", 1, BLACK)
    while True:
        plansza.fill(BETTER_GREEN)
        
        plansza.blit(l_end, (int(rozmiar/2 - 100), int(rozmiar/5-50)))
        plansza.blit(l_score, (int(rozmiar/2 - 200), int(rozmiar/5)))
        plansza.blit(l_newgame, (int(rozmiar/2 - 100), int(2* rozmiar/3)))
        plansza.blit(l_exit, (int(rozmiar/2 - 100), int(2* rozmiar/3)+50))
        

        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 or event.key == pygame.K_ESCAPE:
                    powrot = True
                if event.key == pygame.K_2:
                    pygame.quit()
                    sys.exit()

        if powrot == True:
            break
        pygame.display.update()
        fpsClock.tick(FPS)
        


def multi():
    #zmienne
    v = [-1, 0]
    v2 = [1, 0]
    tab = []
    tab2 = []
    dlugosc = 3
    dlugosc2 = 3

    x = int((rozmiar-2*bok)/20)-2
    y = 2

    x2 = 2
    y2 = int((rozmiar-2*bok)/20)-2
    
    tab = np.zeros((int((rozmiar-2*bok)/20), int((rozmiar-2*bok)/20)))
    tab2 = np.zeros((int((rozmiar-2*bok)/20), int((rozmiar-2*bok)/20)))
    
    essen = np.array([[None, None],
                     [None, None],
                     [None, None],
                     [None, None],
                     [None, None],
                     [None, None],
                     [None, None],
                     [None, None],
                     [None, None],
                     [None, None]])
    n_essen = 0

    licznik = 0
    tab += 5
    tab2 += 5
    
    przegrana = False
    przegrana2 = False

    while True:
        licznik += 1
    
        teren()

        #żarcie
        if licznik % 300 == 0 and n_essen <= 13:
            xz = random.randint(0, int((rozmiar-2*bok)/20-1))
            yz = random.randint(0, int((rozmiar-2*bok)/20-1))
            n_essen += 1
            for i in range(10):
                if essen[i][0] is None:
                    essen[i][0] = xz
                    essen[i][1] = yz
                    break
        

        #grubasy-maker
        for i in range(10):
            if essen[i][0] is not None:
                pygame.draw.rect(plansza, RED, ((essen[i][0]+1) * 20, (essen[i][1]+1) * 20, bok, bok))
                if essen[i][0] == x and essen[i][1] == y:
                    essen[i][0] = None
                    essen[i][1] = None
                    n_essen -= 1
                    dlugosc += 1
                if essen[i][0] == x2 and essen[i][1] == y2:
                    essen[i][0] = None
                    essen[i][1] = None
                    n_essen -= 1
                    dlugosc2 += 1

        #ogon
        for xi in range(int((rozmiar-2*bok)/20)):
            for yi in range(int((rozmiar-2*bok)/20)):
                if tab[xi][yi] <= dlugosc + 1:
                    pygame.draw.rect(plansza, BETTER_GREEN, ((xi+1) * 20, (yi+1) * 20, bok, bok))
                if tab2[xi][yi] <= dlugosc2 + 1:
                    pygame.draw.rect(plansza, YELLOW, ((xi+1) * 20, (yi+1) * 20, bok, bok))
    
        #głowa
        pygame.draw.rect(plansza, GRAY, ((x+1) * 20, (y+1) * 20, bok, bok))
        pygame.draw.rect(plansza, GRAY, ((x2+1) * 20, (y2+1) * 20, bok, bok))
        if licznik % 15 == 0:
            x += v[0] 
            y += v[1]
        if licznik % 15 == 0:
            x2 += v2[0] 
            y2 += v2[1]
        
        
            #przegrana przez wyjście z pola
            if x >= int((rozmiar-2*bok)/20) or y >= int((rozmiar-2*bok)/20) or x < 0 or y < 0:
                przegrana = True
                koniec2(dlugosc,dlugosc2 ,przegrana, przegrana2)
            if x2 >= int((rozmiar-2*bok)/20) or y2 >= int((rozmiar-2*bok)/20) or x2 < 0 or y2 < 0:
                przegrana2 = True
                koniec2(dlugosc,dlugosc2 ,przegrana, przegrana2)

            #przegrana przez ogon
            if tab[x][y] <= dlugosc:
                przegrana = True
            if tab2[x2][y2] <= dlugosc2:
                przegrana2 = True
            
            #przegranie przez wchodzenie innym do dupy
            if tab2[x][y] <= dlugosc2:
                przegrana = True
            if tab[x2][y2] <= dlugosc:
                przegrana2 = True

            #przegrana po zderzeniu sie glowami
            if tab2[x][y] == 0:
                przegrana = True
                przegrana2 = True
            
            tab[x][y] = 0
            tab += 1
            tab2[x2][y2] = 0
            tab2 += 1

            
            
            

    
    

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and licznik > 30:
                if event.key == K_ESCAPE:
                    pass
                if event.key == pygame.K_w:
                    if v == [0, 1]:
                        przegrana = True
                    v = [0, -1]
                if event.key == K_s:
                    if v == [0, -1]:
                        przegrana = True
                    v = [0, 1]
                if event.key == K_d:
                    if v == [-1, 0]:
                        przegrana = True
                    v = [1, 0]
                if event.key == K_a:
                    if v == [1, 0]:
                        przegrana = True
                    v = [-1, 0]
                if event.key == pygame.K_UP:
                    if v2 == [0, 1]:
                        przegrana2 = True
                    v2 = [0, -1]
                if event.key == K_DOWN:
                    if v2 == [0, -1]:
                        przegrana2 = True
                    v2 = [0, 1]
                if event.key == K_RIGHT:
                    if v2 == [-1, 0]:
                        przegrana2 = True
                    v2 = [1, 0]
                if event.key == K_LEFT:
                    if v2 == [1, 0]:
                        przegrana2 = True
                    v2 = [-1, 0]
     

        #przegrana
        if przegrana == True or przegrana2 == True:
            koniec2(dlugosc,dlugosc2 ,przegrana, przegrana2)

        #zegar
        pygame.display.update()
        fpsClock.tick(FPS)


    




































































def main():
    #zmienne
    v = [1, 0]
    tab = []
    dlugosc = 3

    x = 17
    y = 17
    
    tab = np.zeros((int((rozmiar-2*bok)/20), int((rozmiar-2*bok)/20)))
    essen = np.array([[None, None],
                     [None, None],
                     [None, None],
                     [None, None],
                     [None, None],
                     [None, None],
                     [None, None],
                     [None, None],
                     [None, None],
                     [None, None]])
    n_essen = 0

    licznik = 0
    tab += 5
    przegrana = False

    while True:
        licznik += 1
    
        teren()

        #żarcie
        if licznik % 300 == 0 and n_essen <= 13:
            xz = random.randint(0, int((rozmiar-2*bok)/20-1))
            yz = random.randint(0, int((rozmiar-2*bok)/20-1))
            n_essen += 1
            for i in range(10):
                if essen[i][0] is None:
                    essen[i][0] = xz
                    essen[i][1] = yz
                    break
        

        #grubas-maker
        for i in range(10):
            if essen[i][0] is not None:
                pygame.draw.rect(plansza, RED, ((essen[i][0]+1) * 20, (essen[i][1]+1) * 20, bok, bok))
                if essen[i][0] == x and essen[i][1] == y:
                    essen[i][0] = None
                    essen[i][1] = None
                    n_essen -= 1
                    dlugosc += 1

        #ogon
        for xi in range(int((rozmiar-2*bok)/20)):
            for yi in range(int((rozmiar-2*bok)/20)):
                if tab[xi][yi] <= dlugosc + 1:
                    pygame.draw.rect(plansza, BETTER_GREEN, ((xi+1) * 20, (yi+1) * 20, bok, bok))
    
        #głowa
        pygame.draw.rect(plansza, GRAY, ((x+1) * 20, (y+1) * 20, bok, bok))
        if licznik % 15 == 0:
            x += v[0] 
            y += v[1]
        
        
            #przegrana przez wyjście z pola
            if x >= int((rozmiar-2*bok)/20) or y >= int((rozmiar-2*bok)/20) or x < 0 or y < 0:
                koniec(dlugosc)

            #przegrana przez ogon
            if tab[x][y] <= dlugosc:
                przegrana = True
            
            tab[x][y] = 0
            tab += 1

    
    

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and licznik > 30:
                if event.key == K_ESCAPE:
                    pauza(dlugosc)
                if event.key == pygame.K_w:
                    if v == [0, 1]:
                        przegrana = True
                    v = [0, -1]
                if event.key == K_s:
                    if v == [0, -1]:
                        przegrana = True
                    v = [0, 1]
                if event.key == K_d:
                    if v == [-1, 0]:
                        przegrana = True
                    v = [1, 0]
                if event.key == K_a:
                    if v == [1, 0]:
                        przegrana = True
                    v = [-1, 0]
     

        #przegrana
        if przegrana == True:
            koniec(dlugosc)

        #zegar
        pygame.display.update()
        fpsClock.tick(FPS)



#inicjacja
start()
    


    























