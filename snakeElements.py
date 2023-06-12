from enums import *
import pygame 


class Snake:
    def __init__(self, x, y, T):
        self.x = x
        self.y = y
        self.xNorm = x
        self.yNorm = y
        self.v = 1/T
        self.lenght = 1
        self.currentDirection = Direction.NORTH
        self.nextDirection = None
    
    def draw(self, screen, unit, dx, dy):
        pygame.draw.rect(screen, Color.BROWN, (dx+self.xNorm*unit, dy+self.yNorm*unit, unit, unit))
