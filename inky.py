import pygame
from ghost import Ghost

class Inky(Ghost):
    def __init__(self, x, y):
        Ghost.__init__(self)

        self.image = pygame.image.load("img/InkyU1.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.changey = 2
        self.direction  = "U"

        image = pygame.image.load("img/InkyL1.png").convert()
        self.d_left.append(image)
        image = pygame.image.load("img/InkyL2.png").convert()
        self.d_left.append(image)

        image = pygame.image.load("img/InkyR1.png").convert()
        self.d_right.append(image)
        image = pygame.image.load("img/InkyR2.png").convert()
        self.d_right.append(image)

        image = pygame.image.load("img/InkyU1.png").convert()
        self.d_up.append(image)
        image = pygame.image.load("img/InkyU2.png").convert()
        self.d_up.append(image)

        image = pygame.image.load("img/InkyD1.png").convert()
        self.d_down.append(image)
        image = pygame.image.load("img/InkyD2.png").convert()
        self.d_down.append(image)

        self.image = pygame.image.load("img/InkyU1.png").convert()
