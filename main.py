import pygame
import sys
from enums import *
import snakeElements




class Main:
    def __init__(self):

        #zmienne dotyczace okna
        self.screen_width, self.screen_height = 800, 700
        self.unit = 30
        self.running = True

        #zmienne dotyczace gry
        self.mapX, self.mapY = 15, 15
        

        #pygame initialization
        pygame.init()

        #zegar
        self.FPS = 60
        self.clock = pygame.time.Clock()

        #okno
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.RESIZABLE)


    def draw(self):
        #czarne tlo
        self.screen.fill(Color.BLACK)

        #przesuniecie mapy by byla na srodku
        mapWidth, mapHeight = self.unit*self.mapX, self.unit*self.mapY
        dx, dy = (self.screen_width-mapWidth)/2, (self.screen_height-mapHeight)/2

        #rysowanie mapy
        for i in range(self.mapX):
            x = dx + self.unit*i
            for j in range(self.mapY):
                y = dy + self.unit*j
                #zmieniam kolory by byla kratka
                color = Color.GREEN
                if (i+j) % 2 == 0:
                    color = Color.GREEN_LIGHT
                #rysuje kwadracik
                pygame.draw.rect(self.screen, color, (x, y, self.unit, self.unit))
        
        #obramowanie mapy
        pygame.draw.rect(self.screen, Color.GREEN_DARK, (dx-self.unit, dy-self.unit, self.unit, (self.mapY+2)*self.unit))
        pygame.draw.rect(self.screen, Color.GREEN_DARK, (dx+self.unit*self.mapX, dy-self.unit, self.unit, (self.mapY+2)*self.unit))
        pygame.draw.rect(self.screen, Color.GREEN_DARK, (dx, dy-self.unit, self.mapX*self.unit, self.unit))
        pygame.draw.rect(self.screen, Color.GREEN_DARK, (dx, dy+self.mapY*self.unit, self.mapX*self.unit, self.unit))

        #rysowanie gracza
        
                



        


    def run(self):

        #glowna petla
        while self.running:
            
            #rysuje
            self.draw()


            #przechwytywanie zdarzen
            for event in pygame.event.get():
                #zamykanie okna
                if event.type == pygame.QUIT:
                    self.running = False
                    sys.exit()

            #odswiezanie okna
            pygame.display.update()

            #kontroluje FPS
            self.clock.tick(self.FPS)
        

        #poza glowna petla koncze dzialanie pygame
        pygame.quit()





#uruchamiam gre
game = Main()
game.run()




