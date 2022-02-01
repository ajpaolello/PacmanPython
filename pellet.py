import pygame

class Pellet(pygame.sprite.Sprite):
    """Creates pellet object which will be used for pellet list later"""
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load("img/PowerPellet.png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
