import pygame

BLACK = (0, 0, 0)

class Pacman(pygame.sprite.Sprite):
    """Create a pacman object with animations, directions, speed,
    and setting colllisons with walls"""
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/PacManClose.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = 289
        self.rect.y = 453
        self.changex = 0
        self.changey = 0
        self.d_left = []
        self.d_right= []
        self.d_up = []
        self.d_down = []
        self.direction  = "N"
        self.walls = None


        image = pygame.image.load("img/PacManMinLeft.png").convert()
        self.d_left.append(image)
        image = pygame.image.load("img/PacManMaxLeft.png").convert()
        self.d_left.append(image)
        image = pygame.image.load("img/PacManMinLeft.png").convert()
        self.d_left.append(image)
        image = pygame.image.load("img/PacManCloseLeft.png").convert()
        self.d_left.append(image)

        image = pygame.image.load("img/PacManMinRight.png").convert()
        self.d_right.append(image)
        image = pygame.image.load("img/PacManMaxRight.png").convert()
        self.d_right.append(image)
        image = pygame.image.load("img/PacManMinRight.png").convert()
        self.d_right.append(image)
        image = pygame.image.load("img/PacManCloseRight.png").convert()
        self.d_right.append(image)

        image = pygame.image.load("img/PacManMinUp.png").convert()
        self.d_up.append(image)
        image = pygame.image.load("img/PacManMaxUp.png").convert()
        self.d_up.append(image)
        image = pygame.image.load("img/PacManMinUp.png").convert()
        self.d_up.append(image)
        image = pygame.image.load("img/PacManCloseUp.png").convert()
        self.d_up.append(image)

        image = pygame.image.load("img/PacManMinDown.png").convert()
        self.d_down.append(image)
        image = pygame.image.load("img/PacManMaxDown.png").convert()
        self.d_down.append(image)
        image = pygame.image.load("img/PacManMinDown.png").convert()
        self.d_down.append(image)
        image = pygame.image.load("img/PacManCloseDown.png").convert()
        self.d_down.append(image)

        self.image = pygame.image.load("img/PacManClose.png").convert()
        self.image.set_colorkey(BLACK)

    def moveLeft(self):
        """Move left"""
        self.direction = "L"
        self.changex = -2
        self.changey = 0

    def moveRight(self):
        """Move right"""
        self.direction = "R"
        self.changex = 2
        self.changey = 0

    def moveUp(self):
        """Move up"""
        self.direction = "U"
        self.changey = -2
        self.changex = 0

    def moveDown(self):
        """Move down"""
        self.direction = "D"
        self.changey = 2
        self.changex = 0

    def update(self):
        """Update function"""
        #Speed variable
        self.rect.x += self.changex
        pos1 = self.rect.x
        #Runs the animation with division and modulus
        if self.direction == "R":
            frame = (pos1 // 4) % len(self.d_right)
            self.image = self.d_right[frame]
            self.image.set_colorkey(BLACK)
        elif self.direction == "L":
            frame = (pos1 // 4) % len(self.d_left)
            self.image = self.d_left[frame]
            self.image.set_colorkey(BLACK)

        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)

        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
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

        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.changey > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
        if self.rect.x > 557:
            self.rect.x = 44
        if self.rect.x < 44:
            self.rect.x = 557
