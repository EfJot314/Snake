import pygame
import sys
import random as rnd
from enums import *
import GameElements




class Main:
    def __init__(self):

        #pygame initialization
        pygame.init()

        #zmienne dotyczace okna
        self.screen_width, self.screen_height = 800, 700
        self.unit = 30
        self.running = True
        self.font = pygame.font.Font('freesansbold.ttf', 30)


        #zegar
        self.FPS = 60
        self.clock = pygame.time.Clock()

        #okno
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.RESIZABLE)
        pygame.display.set_caption("Snake")
        

        #zmienne dotyczace gry
        self.mapX, self.mapY = 15, 15
        self.T = self.FPS / 4
        self.apple = None
        self.score = 0

        #gracz
        self.player = GameElements.Snake(7, 7, self.T)

    def drawAll(self):
        #pobieram rozmiary okna
        self.screen_width, self.screen_height = self.screen.get_size()

        #obliczam wartosc jednostki
        size = min(self.screen_width, self.screen_height)
        self.unit = max(int(size/20), 10)

        #czarne tlo
        self.screen.fill(BLACK)

        #score
        scoreText = self.font.render("Score: "+str(self.score), True, WHITE)
        self.screen.blit(scoreText, (10,10))

        #przesuniecie mapy by byla na srodku
        mapWidth, mapHeight = self.unit*self.mapX, self.unit*self.mapY
        dx, dy = (self.screen_width-mapWidth)/2, (self.screen_height-mapHeight)/2

        #rysowanie mapy
        for i in range(self.mapX):
            x = dx + self.unit*i
            for j in range(self.mapY):
                y = dy + self.unit*j
                #zmieniam kolory by byla kratka
                color = GREEN
                if (i+j) % 2 == 0:
                    color = GREEN_LIGHT
                #rysuje kwadracik
                pygame.draw.rect(self.screen, color, (x, y, self.unit, self.unit))
        
        #obramowanie mapy
        pygame.draw.rect(self.screen, GREEN_DARK, (dx-self.unit, dy-self.unit, self.unit, (self.mapY+2)*self.unit))
        pygame.draw.rect(self.screen, GREEN_DARK, (dx+self.unit*self.mapX, dy-self.unit, self.unit, (self.mapY+2)*self.unit))
        pygame.draw.rect(self.screen, GREEN_DARK, (dx, dy-self.unit, self.mapX*self.unit, self.unit))
        pygame.draw.rect(self.screen, GREEN_DARK, (dx, dy+self.mapY*self.unit, self.mapX*self.unit, self.unit))

        #rysowanie jablka
        if self.apple != None:
            self.apple.draw(self.screen, self.unit, dx, dy)

        #rysowanie gracza
        self.player.draw(self.screen, self.unit, dx, dy)
                
    def generateApple(self):
        if self.apple == None:
            found = False
            while not found:
                #losuje wspolrzedne jablka
                x = rnd.randint(0, self.mapX-1)
                y = rnd.randint(0, self.mapY-1)

                #sprawdzam czy nie chce wygenerowac jablka w wezu
                found = True
                if self.player.x == x and self.player.y == y:
                    found = False
                elif abs(self.player.xNorm-x) < 0.9 and abs(self.player.yNorm-y) < 0.9: #tu sprawdzam czy wlasnie nie wchodze na pole z ewentulanym jablkiem
                    found = False
                else:
                    for tailElement in self.player.tail:
                        if tailElement.x == x and tailElement.y == y:
                            found = False
                            break
                
                #jesli wszystko ok, to tworze jablko
                if found:
                    self.apple = GameElements.Apple(x, y)

    def eatApple(self):
        if self.player.x == self.apple.x and self.player.y == self.apple.y:
            self.score += 1
            self.apple = None
            self.player.addTailElement()
        
    def run(self):

        #licznik iteracji
        self.counter = 0

        #glowna petla
        while self.running:
            #rysuje
            self.drawAll()

            #ewentualnie generuje jablko
            self.generateApple()

            #poruszam gracza
            self.player.move()
            if self.counter % self.T == 0:
                self.counter = (self.counter) % 10000
                self.player.confirmPosition()
                #ewentualne jedzenie jablka
                self.eatApple()

            #ewentualny koniec gry
            if self.player.checkGameOver(self.mapX, self.mapY):
                self.running = False
                
            #przechwytywanie zdarzen
            for event in pygame.event.get():
                #zamykanie okna
                if event.type == pygame.QUIT:
                    self.running = False
                    # sys.exit()
                #klikniecia przyciskow
                elif event.type == pygame.KEYDOWN:
                    #WSAD
                    if event.key == pygame.K_w:
                        self.player.nextDirection = Direction.NORTH
                    elif event.key == pygame.K_d:
                        self.player.nextDirection = Direction.EAST
                    elif event.key == pygame.K_s:
                        self.player.nextDirection = Direction.SOUTH
                    elif event.key == pygame.K_a:
                        self.player.nextDirection = Direction.WEST
                
            
            #inkrementacja licznika
            self.counter += 1

            #odswiezanie okna
            pygame.display.update()

            #kontroluje FPS
            self.clock.tick(self.FPS)
        

        #poza glowna petla koncze dzialanie pygame
        pygame.quit()





#uruchamiam gre
game = Main()
game.run()




