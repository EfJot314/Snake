from enums import *
import pygame 


class Apple:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self, screen, unit, dx, dy):
        pygame.draw.circle(screen, RED, (dx+(self.x+0.5)*unit, dy+(self.y+0.5)*unit), unit/3)




class SnakeElement:
    def __init__(self, x, y, v):
        #pozycja
        self.x = x
        self.y = y
        self.xNorm = self.x
        self.yNorm = self.y
        #szybkosc poruszania sie (kratki/klatke)
        self.v = v
        #kierunki poruszania sie
        self.currentDirection = Direction.NORTH
        self.nextDirection = None
    
    def draw(self, screen, unit, dx, dy, color):
        pygame.draw.rect(screen, color, (dx+self.xNorm*unit, dy+self.yNorm*unit, unit, unit))

    def move(self):
        #zmieniam pozycje wzgledna o pewna wartosc v
        if self.currentDirection == Direction.NORTH:
            self.yNorm -= self.v
        elif  self.currentDirection == Direction.EAST:
            self.xNorm += self.v
        elif  self.currentDirection == Direction.SOUTH:
            self.yNorm += self.v
        elif  self.currentDirection == Direction.WEST:
            self.xNorm -= self.v
        
    def confirmPosition(self):
        #zmiana pozycji
        if self.currentDirection == Direction.NORTH:
            self.y -= 1
        elif  self.currentDirection == Direction.EAST:
            self.x += 1
        elif  self.currentDirection == Direction.SOUTH:
            self.y += 1
        elif  self.currentDirection == Direction.WEST:
            self.x -= 1

        #ustalenie pozycji wzglednej (aby pozbyc sie bledow przyblizen)
        self.xNorm = self.x
        self.yNorm = self.y

        #ustalenie aktualnego kierunku
        if self.nextDirection != None:
            self.currentDirection = self.nextDirection
            self.nextDirection = None

    def resetPosition(self, x, y):
        #przywracam glowne zmienne do ustawien poczatkowych
        self.x = x
        self.y = y
        self.xNorm = self.x
        self.yNorm = self.y
        self.currentDirection = Direction.NORTH
        self.nextDirection = None




class Snake(SnakeElement):
    def __init__(self, x, y, T):
        super().__init__(x, y, 1/T)
        self.tail = [
                        SnakeTailElement(self.x, self.y+1, self.v),
                        SnakeTailElement(self.x, self.y+2, self.v)
                    ]
        self.bendElements = []
        self.newElement = None

    def move(self):
        super().move()
        for tailElement in self.tail:
            tailElement.move()

    def confirmPosition(self):
        #usuwam zgiecia
        self.bendElements = []

        #dodaje ewentualny nowy element do ogona
        if self.newElement != None:
            self.newElement.currentDirection = None
            self.tail.append(self.newElement)
            self.newElement = None

        #zmieniam kierunki mojemu ogonowi
        self.tail[0].nextDirection = self.currentDirection
        for i in range(1, len(self.tail)):
            self.tail[i].nextDirection = self.tail[i-1].currentDirection

        
        
        #ustalam pozycje
        super().confirmPosition()
        for tailElement in self.tail:
            tailElement.confirmPosition()


        #jezeli jest gdzies zagiecie to je zapelniam, by waz byl jednoscia
        if self.currentDirection != self.tail[0].currentDirection:
            self.bendElements.append(SnakeTailElement(self.x, self.y, 0))
        for i in range(1, len(self.tail)):
            if self.tail[i].currentDirection != self.tail[i-1].currentDirection:
                x, y = self.tail[i-1].x, self.tail[i-1].y
                self.bendElements.append(SnakeTailElement(x, y, 0))

    def checkGameOver(self, nX, nY):
        #wyjscie z mapy gora-lewo
        if self.x < 0 or self.y < 0:
            return True
        #wyjscie z mapy dol-prawo
        if self.x >= nX or self.y >= nY:
            return True
        #zderzenie z wlasnym ogonem
        for tailElement in self.tail:
            if tailElement.x == self.x and tailElement.y == self.y:
                return True
        #jesli wszystko ok, to zwracam ze nie ma powodu do zakonczenia gry
        return False
        

    def addTailElement(self):
        lastElement = self.tail[len(self.tail)-1]
        self.newElement = SnakeTailElement(lastElement.x, lastElement.y, self.v)
        
    def draw(self, screen, unit, dx, dy):
        #ogon
        for tailElement in self.tail:
            tailElement.draw(screen, unit, dx, dy)
        #zagiecia
        for tailElement in self.bendElements:
            tailElement.draw(screen, unit, dx, dy)
        #ewentualny nowy element
        if self.newElement != None:
            self.newElement.draw(screen, unit, dx, dy)
        #glowa
        super().draw(screen, unit, dx, dy, BROWN)



    

class SnakeTailElement(SnakeElement):
    def draw(self, screen, unit, dx, dy):
        super().draw(screen, unit, dx, dy, BROWN_LIGHT)
    

        