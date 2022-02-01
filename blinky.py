import pygame
from ghost import Ghost

class Blinky(Ghost):
    def __init__(self, x, y):
        Ghost.__init__(self)

        self.image = pygame.image.load("img/BlinkyR1.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.changex = 2
        self.direction  = "R"

        image = pygame.image.load("img/BlinkyL1.png").convert()
        self.d_left.append(image)
        image = pygame.image.load("img/BlinkyL2.png").convert()
        self.d_left.append(image)

        image = pygame.image.load("img/BlinkyR1.png").convert()
        self.d_right.append(image)
        image = pygame.image.load("img/BlinkyR2.png").convert()
        self.d_right.append(image)

        image = pygame.image.load("img/BlinkyU1.png").convert()
        self.d_up.append(image)
        image = pygame.image.load("img/BlinkyU2.png").convert()
        self.d_up.append(image)

        image = pygame.image.load("img/BlinkyD1.png").convert()
        self.d_down.append(image)
        image = pygame.image.load("img/BlinkyD2.png").convert()
        self.d_down.append(image)

        self.image = pygame.image.load("img/BlinkyR1.png").convert()


