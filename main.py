import pygame
import sys

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW_LIGHT = (255, 255, 102)
YELLOW = (255, 255, 0)
GREY = (211, 211, 211)
ORANGE = (255, 69, 0)
PINK = (255, 105, 180)




class Main:
    def __init__(self):



        #definicja zmiennych
        self.screen_width, self.screen_height = 800, 700



        #pygame initialization
        pygame.init()

        #zegar
        self.FPS = 60
        self.clock = pygame.time.Clock()

        #okno
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.RESIZABLE)

    def run(self):


        #glowna petla
        while True:
            self.screen.fill(RED)
            


            #przechwytywanie zdarzen
            for event in pygame.event.get():
                #zamykanie okna
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            #odswiezanie okna
            pygame.display.update()

            #kontroluje FPS
            self.clock.tick(self.FPS)





#uruchamiam gre
game = Main()
game.run()




