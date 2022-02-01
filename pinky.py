import pygame
from ghost import Ghost

class Pinky(Ghost):
    def __init__(self, x, y):
        Ghost.__init__(self)

        self.image = pygame.image.load("img/PinkyR1.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.changex = -2
        self.direction  = "L"

        image = pygame.image.load("img/PinkyL1.png").convert()
        self.d_left.append(image)
        image = pygame.image.load("img/PinkyL2.png").convert()
        self.d_left.append(image)

        image = pygame.image.load("img/PinkyR1.png").convert()
        self.d_right.append(image)
        image = pygame.image.load("img/PinkyR2.png").convert()
        self.d_right.append(image)

        image = pygame.image.load("img/PinkyU1.png").convert()
        self.d_up.append(image)
        image = pygame.image.load("img/PinkyU2.png").convert()
        self.d_up.append(image)

        image = pygame.image.load("img/PinkyD1.png").convert()
        self.d_down.append(image)
        image = pygame.image.load("img/PinkyD2.png").convert()
        self.d_down.append(image)

        self.image = pygame.image.load("img/PinkyL1.png").convert()
