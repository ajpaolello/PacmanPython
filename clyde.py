import pygame
from ghost import Ghost

class Clyde(Ghost):
    def __init__(self, x, y):
        Ghost.__init__(self)

        self.image = pygame.image.load("img/ClydeD1.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.changey = 2
        self.direction  = "D"

        image = pygame.image.load("img/ClydeL1.png").convert()
        self.d_left.append(image)
        image = pygame.image.load("img/ClydeL2.png").convert()
        self.d_left.append(image)

        image = pygame.image.load("img/ClydeR1.png").convert()
        self.d_right.append(image)
        image = pygame.image.load("img/ClydeR2.png").convert()
        self.d_right.append(image)

        image = pygame.image.load("img/ClydeU1.png").convert()
        self.d_up.append(image)
        image = pygame.image.load("img/ClydeU2.png").convert()
        self.d_up.append(image)

        image = pygame.image.load("img/ClydeD1.png").convert()
        self.d_down.append(image)
        image = pygame.image.load("img/ClydeD2.png").convert()
        self.d_down.append(image)

        self.image = pygame.image.load("img/ClydeD1.png").convert()
