import pygame
import random

BLACK = (0, 0, 0)

class Ghost(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.direction = None
        self.changex = 0
        self.changey = 0
        self.d_left = []
        self.d_right= []
        self.d_up = []
        self.d_down = []
        self.walls = None
        self.sidehit = False
        self.tophit = False

    def moveLeft(self):
        self.direction = "L"
        self.changex = -2
        self.changey = 0

    def moveRight(self):
        self.direction = "R"
        self.changex = 2
        self.changey = 0

    def moveUp(self):
        self.direction = "U"
        self.changex = 0
        self.changey = -2

    def moveDown(self):
        self.direction = "D"
        self.changex = 0
        self.changey = 2
    
    def update(self):
        directnum = random.randrange(4)
        if self.sidehit == True or self.tophit == True:
            if directnum == 0:
                self.moveLeft()
            elif directnum == 1:
                self.moveRight()
            elif directnum == 2:
                self.moveUp()
            elif directnum == 3:
                self.moveDown()

        self.sidehit = False
        self.tophit = False
        self.rect.x += self.changex
        pos1 = self.rect.x
        if self.direction == "R":
            frame = (pos1 // 4) % len(self.d_right)
            self.image = self.d_right[frame]
            self.image.set_colorkey(BLACK)
        elif self.direction == "L":
            frame = (pos1 // 4) % len(self.d_left)
            self.image = self.d_left[frame]
            self.image.set_colorkey(BLACK)

        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self,
                self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            self.sidehit = True
            if self.changex > 0:
                self.rect.right = block.rect.left

            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        self.rect.y += self.changey
        pos2 = self.rect.y
        if self.direction == "U":
            frame = (pos2 // 4) % len(self.d_up)
            self.image = self.d_up[frame]
            self.image.set_colorkey(BLACK)
        elif self.direction == "D":
            frame = (pos2 // 4) % len(self.d_down)
            self.image = self.d_down[frame]
            self.image.set_colorkey(BLACK)

        block_hit_list = pygame.sprite.spritecollide(self,
                self.walls, False)
        for block in block_hit_list:
            self.tophit = True

            # Reset our position based on the top/bottom of the object.
            if self.changey > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

