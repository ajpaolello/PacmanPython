import pygame
from pacman import Pacman
from wall import Wall
from pellet import Pellet
from blinky import Blinky
from pinky import Pinky
from inky import Inky
from clyde import Clyde


def game():
    """Main function"""

    # Create our boolean while condition
    done = False

    # Create the sound when pacman eats a pellet
    munch = {0: pygame.mixer.Sound("audio/munch_1.wav"), 1: pygame.mixer.Sound("audio/munch_2.wav")}
    munchnum = 0

    # Background sound
    background_sound = pygame.mixer.Sound("audio/background_sound_new.ogg")

    # Create a list for all the pellets
    pellet_list = make_pellets()

    # Create a list for the walls    
    wall_list = make_walls()

    # Create Pacman and Ghosts with starting locations
    pacman = Pacman()
    blinky = Blinky(50, 110)
    pinky = Pinky(450, 110)
    inky = Inky(50, 725)
    clyde = Clyde(450, 725)

    # Assign the list of walls to the walls variable 
    # in pacman and the ghosts
    # This will allow them to stop when they hit a wall 
    # (or do other actions for the ghosts)
    pacman.walls = wall_list
    blinky.walls = wall_list
    pinky.walls = wall_list
    inky.walls = wall_list
    clyde.walls = wall_list

    # Create a list of ghosts and add each ghost
    ghost_list = pygame.sprite.Group()
    ghost_list.add(blinky)
    ghost_list.add(pinky)
    ghost_list.add(inky)
    ghost_list.add(clyde)

    # Create a variable to track score
    score = 0

    highscore = 1000

    # Lives that the player has
    lives = 3

    life_icon = pygame.image.load("img/PacManMinRight.png")
    background_sound.play(-1)
    # Main Game Loop
    while not done:
        for event in pygame.event.get():
            # Move Pacman based on key    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pacman.moveLeft()

                if event.key == pygame.K_RIGHT:
                    pacman.moveRight()

                if event.key == pygame.K_UP:
                    pacman.moveUp()

                if event.key == pygame.K_DOWN:
                    pacman.moveDown()

                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    done = True

            # Stops Pacman. This leads to needing to delay direction change
            # But also prevents diagonal movement.
            elif event.type == pygame.KEYUP:
                pacman.changex = 0
                pacman.changey = 0

        # Paint it black                   
        screen.fill((0, 0, 0))

        font = pygame.font.SysFont('comicsansms', 25, True, False)
        score_label = font.render("HIGH SCORE", True, (255, 255, 255))
        high_score = font.render(str(highscore), True, (255, 255, 255))
        one_up_label = font.render("1UP", True, (255, 255, 255))
        score_text = font.render(str(score), True, (255, 255, 255))

        win_text = font.render("You Win!", True, (255, 255, 255))
        pacman.update()
        ghost_list.update()
        wall_list.update()
        pellet_list.update()

        # Check collision between pacman and pellets,
        # remove pellet if collides.
        # Also, if collided, play sound and increase score by 1
        # If score equals the max pellets, print the win text 
        # and end the game

        block_hit_list = pygame.sprite.spritecollide(pacman, pellet_list,
                                                     True)

        for _ in block_hit_list:
            score += 10
            munch[munchnum].play()
            munchnum = 1 - munchnum
            if not pellet_list:
                screen.blit(win_text, [250, 470])
                done = True

        # Check if pacman collides with a ghost, but don't delete the ghost
        # If hit, display game over text and end the game
        block_hit_list2 = pygame.sprite.spritecollide(pacman, ghost_list,
                                                      False)
        for _ in block_hit_list2:
            lives -= 1
            pacman = Pacman()
            pacman.walls = wall_list
            if lives == 0:
                done = True

        if score > highscore:
            highscore = score
        # Print the score and the given location
        screen.blit(score_label, [250, 30])
        screen.blit(high_score, [280, 60])
        screen.blit(one_up_label, [44, 30])
        screen.blit(score_text, [55, 60])

        for life in range(lives):
            screen.blit(life_icon, [10 + (life * 30), 770])
        pellet_list.draw(screen)
        ghost_list.draw(screen)
        wall_list.draw(screen)
        screen.blit(pacman.image, (pacman.rect.x, pacman.rect.y))

        pygame.display.flip()

        # 60 FPS for an arcade game seems about right
        clock.tick(60)

    background_sound.stop()
    gameover()


def menu():
    """ Display main menu """
    font = pygame.font.SysFont('comicsansm', 36, True, False)
    title_font = pygame.font.SysFont('comicsansm', 100, True, False)
    title_text = title_font.render("Pac-Man", True, (255, 255, 255))
    enter_text = font.render("Press ENTER to play", True, (255, 255, 255))
    quit_text = font.render("Press Q to quit", True, (255, 255, 255))

    menu_image = pygame.image.load('img/titleGraphic_scaled.jpg').convert()

    screen.blit(title_text, (138, 150))
    screen.blit(menu_image, (0, 300))
    screen.blit(enter_text, (150, 600))
    screen.blit(quit_text, (170, 650))

    menu_music = pygame.mixer.Sound('audio/pacman_intermission.ogg')
    menu_music.set_volume(0.25)
    menu_music.play(-1)

    pygame.display.update()

    while True:
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                menu_music.stop()
                game()
                break
            elif event.key == pygame.K_q:
                exit()


def make_pellets():
    pellet_list = pygame.sprite.Group()

    left_top_row = [[66, 103], [85, 103], [104, 103], [123, 103],
                    [142, 103], [161, 103], [180, 103], [199, 103], [218, 103],
                    [237, 103], [256, 103], [275, 103]]

    right_top_row = [[332, 103], [351, 103], [370, 103], [389, 103],
                     [408, 103], [427, 103], [446, 103], [465, 103], [484, 103],
                     [503, 103], [522, 103], [541, 103]]

    top_left_vertical = [[66, 122], [66, 141], [66, 160], [66, 179],
                         [66, 198], [66, 217], [66, 236], [66, 255]]

    upper_mid_horizontal_row = [[85, 198], [104, 198], [123, 198],
                                [142, 198], [161, 198], [180, 198], [199, 198], [218, 198],
                                [237, 198], [256, 198], [275, 198], [294, 198], [313, 198],
                                [332, 198], [351, 198], [370, 198], [389, 198], [408, 198],
                                [427, 198], [446, 198], [465, 198], [484, 198], [503, 198],
                                [522, 198], [541, 198]]

    left_vertical = [[161, 122], [161, 141], [161, 160], [161, 179],
                     [161, 217], [161, 236], [161, 255], [161, 274], [161, 293],
                     [161, 312], [161, 331], [161, 350], [161, 369], [161, 388],
                     [161, 407], [161, 426], [161, 445], [161, 464], [161, 483],
                     [161, 502], [161, 521], [161, 540], [161, 559], [161, 578],
                     [161, 597], [161, 616], [161, 635], [161, 654], [161, 673]]

    right_vertical = [[446, 122], [446, 141], [446, 160], [446, 179],
                      [446, 217], [446, 236], [446, 255], [446, 274], [446, 293],
                      [446, 312], [446, 331], [446, 350], [446, 369], [446, 388],
                      [446, 407], [446, 426], [446, 445], [446, 464], [446, 483],
                      [446, 502], [446, 521], [446, 540], [446, 559], [446, 578],
                      [446, 597], [446, 616], [446, 635], [446, 654], [446, 673]]

    top_lower_left = [[85, 255], [104, 255], [123, 255], [142, 255]]

    upper_box_left_vertical = [[275, 122], [275, 141], [275, 160],
                               [275, 179]]

    upper_box_right_vertical = [[332, 122], [332, 141], [332, 160],
                                [332, 179]]

    top_right_vertical = [[541, 122], [541, 141], [541, 160], [541, 179],
                          [541, 217], [541, 236], [541, 255]]

    top_lower_right = [[465, 255], [484, 255], [503, 255], [522, 255]]

    ghost_cage_left_upper_l = [[218, 217], [218, 236], [218, 255],
                               [218, 274], [237, 274], [256, 274], [275, 274]]

    ghost_cage_right_upper_l = [[389, 217], [389, 236], [389, 255],
                                [389, 274], [370, 274], [351, 274], [332, 274]]

    lower_left_upper_row = [[66, 521], [85, 521], [104, 521],
                            [123, 521], [142, 521], [180, 521], [199, 521], [218, 521],
                            [237, 521], [256, 521], [275, 521]]

    lower_right_upper_row = [[332, 521], [351, 521], [370, 521],
                             [389, 521], [408, 521], [427, 521], [446, 521], [465, 521],
                             [484, 521], [503, 521], [522, 521], [541, 521]]

    bottom_upper_middle_row = [[180, 597], [199, 597], [218, 597], [237, 597],
                               [256, 597], [275, 597], [294, 597], [313, 597], [332, 597], [351, 597],
                               [370, 597], [389, 597], [408, 597], [427, 597]]

    bottom_lower_middle_row_left = [[66, 673], [85, 673], [104, 673], [123, 673],
                                    [142, 673]]

    bottom_lower_middle_row_right = [[465, 673], [484, 673], [503, 673],
                                     [522, 673], [541, 673]]

    bottom_left_tetris_piece = [[66, 540], [66, 559], [66, 578], [66, 597],
                                [85, 597], [104, 597], [104, 616], [104, 635], [104, 654]]

    bottom_right_tetris_piece = [[541, 540], [541, 559], [541, 578], [541, 597],
                                 [522, 597], [503, 597], [503, 616], [503, 635], [503, 654]]

    bottom_upside_down_t_left_l = [[218, 616], [218, 635], [218, 654], [218, 673],
                                   [237, 673], [256, 673], [275, 673], [275, 692], [275, 711]]

    bottom_upside_down_t_right_l = [[389, 616], [389, 635], [389, 654], [389, 673],
                                    [370, 673], [351, 673], [332, 673], [332, 692], [332, 711]]

    lower_middle_t_vertical_left = [[275, 540], [275, 559], [275, 578]]

    lower_middle_t_vertical_right = [[332, 540], [332, 559], [332, 578]]

    bottom_vertical_left = [[66, 692], [66, 711]]

    bottom_vertical_right = [[541, 692], [541, 711]]

    bottom_row = [[66, 730], [85, 730], [104, 730], [123, 730],
                  [142, 730], [161, 730], [180, 730], [199, 730], [218, 730],
                  [237, 730], [256, 730], [275, 730], [294, 730], [313, 730],
                  [332, 730], [351, 730], [370, 730], [389, 730], [408, 730],
                  [427, 730], [446, 730], [465, 730], [484, 730], [503, 730],
                  [522, 730], [541, 730]]

    pellet_map = [left_top_row, right_top_row, top_left_vertical,
                  upper_mid_horizontal_row, left_vertical, right_vertical, top_lower_left,
                  upper_box_left_vertical, upper_box_right_vertical, top_right_vertical,
                  top_lower_right, ghost_cage_left_upper_l, ghost_cage_right_upper_l,
                  lower_left_upper_row, lower_right_upper_row, bottom_upper_middle_row,
                  bottom_lower_middle_row_left, bottom_lower_middle_row_right, bottom_left_tetris_piece,
                  bottom_right_tetris_piece, bottom_upside_down_t_left_l, bottom_upside_down_t_right_l,
                  lower_middle_t_vertical_left, lower_middle_t_vertical_right, bottom_vertical_left,
                  bottom_vertical_right, bottom_row]
    for group in pellet_map:
        for pellet in group:
            new_pellet = Pellet(pellet[0], pellet[1])
            pellet_list.add(new_pellet)

    print(len(pellet_list))
    return pellet_list


def make_walls():
    wall_list = pygame.sprite.Group()

    top_row = [44, 84, 520, 5]
    upper_box_left = [294, 84, 5, 85]
    upper_box_right = [313, 84, 5, 85]
    upper_box_bottom = [294, 169, 24, 5]
    top_left_vertical = [44, 84, 5, 200]
    top_right_vertical = [564, 84, 5, 200]
    top_left_lower = [44, 280, 100, 5]
    top_right_lower = [468, 280, 100, 5]
    upper_mid_left_vertical = [140, 280, 5, 92]
    upper_mid_right_vertical = [468, 280, 5, 92]
    upper_mid_right_lower = [468, 369, 100, 5]
    upper_mid_left_lower = [44, 369, 100, 5]
    lower_mid_left_top = [44, 419, 100, 5]
    lower_mid_right_top = [470, 419, 100, 5]
    lower_mid_left_vertical = [140, 420, 5, 82]
    lower_mid_right_vertical = [468, 420, 5, 82]
    lower_mid_left_lower = [44, 500, 100, 5]
    lower_mid_right_lower = [468, 500, 100, 5]
    bottom_left_vertical = [44, 504, 5, 250]
    bottom_right_vertical = [564, 500, 5, 250]
    bottom_row = [44, 750, 525, 5]
    top_left_medium_box_top = [90, 127, 55, 5]
    top_left_medium_box_left = [90, 127, 5, 43]
    top_left_medium_box_right = [141, 127, 5, 43]
    top_left_medium_box_bottom = [90, 165, 55, 5]
    top_right_medium_box_top = [471, 127, 55, 5]
    top_right_medium_box_left = [471, 127, 5, 43]
    top_right_medium_box_right = [522, 127, 5, 43]
    top_right_medium_box_bottom = [471, 165, 55, 5]
    top_left_large_box_top = [189, 127, 73, 5]
    top_left_large_box_left = [189, 127, 5, 43]
    top_left_large_box_right = [260, 127, 5, 48]
    top_left_large_box_bottom = [189, 170, 73, 5]
    top_right_large_box_top = [348, 127, 73, 5]
    top_right_large_box_left = [348, 127, 5, 43]
    top_right_large_box_right = [421, 127, 5, 48]
    top_right_large_box_bottom = [348, 170, 73, 5]
    top_left_small_box_top = [90, 220, 55, 5]
    top_left_small_box_left = [90, 220, 5, 20]
    top_left_small_box_right = [140, 220, 5, 20]
    top_left_small_box_bottom = [90, 240, 55, 5]
    top_right_small_box_top = [473, 220, 55, 5]
    top_right_small_box_left = [473, 220, 5, 20]
    top_right_small_box_right = [523, 220, 5, 20]
    top_right_small_box_bottom = [473, 240, 55, 5]
    upper_middle_t_top = [240, 220, 132, 5]
    upper_middle_t_top_left = [240, 220, 5, 25]
    upper_middle_t_top_right = [368, 220, 5, 25]
    upper_middle_t_upper_left_bottom = [240, 240, 59, 5]
    upper_middle_t_upper_right_bottom = [313, 240, 57, 5]
    upper_middle_t_bottom_left = [294, 240, 5, 70]
    upper_middle_t_bottom_right = [313, 240, 5, 70]
    upper_middle_t_bottom = [294, 305, 20, 5]
    left_t_top = [181, 221, 20, 5]
    left_t_left_vertical = [181, 221, 5, 165]
    left_t_right_upper_vertical = [196, 221, 5, 78]
    left_t_right_upper_horizontal = [196, 294, 60, 5]
    left_t_right_vertical = [251, 294, 5, 20]
    left_t_right_lower_horizontal = [196, 313, 60, 5]
    left_t_right_lower_vertical = [196, 317, 5, 69]
    left_t_bottom = [181, 383, 20, 5]
    right_t_top = [407, 221, 20, 5]
    right_t_right_vertical = [422, 221, 5, 165]
    right_t_left_upper_vertical = [407, 221, 5, 78]
    right_t_left_upper_horizontal = [353, 294, 54, 5]
    right_t_left_vertical = [353, 294, 5, 20]
    right_t_left_lower_horizontal = [353, 313, 59, 5]
    right_t_left_lower_vertical = [407, 317, 5, 69]
    right_t_bottom = [407, 383, 20, 5]
    left_vertical_box_top = [181, 417, 20, 5]
    left_vertical_box_left = [181, 417, 5, 90]
    left_vertical_box_right = [196, 417, 5, 90]
    left_vertical_box_bottom = [181, 502, 20, 5]
    right_vertical_box_top = [407, 417, 20, 5]
    right_vertical_box_left = [407, 417, 5, 90]
    right_vertical_box_right = [422, 417, 5, 90]
    right_vertical_box_bottom = [407, 502, 20, 5]
    lower_middle_t_top = [240, 485, 132, 5]
    lower_middle_t_upper_left = [240, 485, 5, 25]
    lower_middle_t_upper_right = [368, 485, 5, 25]
    lower_middle_t_left_horizontal = [240, 505, 59, 5]
    lower_middle_t_right_horizontal = [313, 505, 57, 5]
    lower_middle_t_lower_left = [294, 505, 5, 70]
    lower_middle_t_lower_right = [313, 505, 5, 70]
    lower_middle_t_bottom = [294, 570, 20, 5]
    bottom_middle_t_top = [240, 628, 132, 5]
    bottom_middle_t_upper_left = [240, 628, 5, 25]
    bottom_middle_t_upper_right = [368, 628, 5, 25]
    bottom_middle_t_left_horizontal = [240, 648, 59, 5]
    bottom_middle_t_right_horizontal = [313, 648, 57, 5]
    bottom_middle_t_lower_left = [294, 648, 5, 70]
    bottom_middle_t_lower_right = [313, 648, 5, 70]
    bottom_middle_t_bottom = [294, 713, 20, 5]
    left_horizontal_box_top = [181, 551, 75, 5]
    left_horizontal_box_left = [181, 551, 5, 25]
    left_horizontal_box_right = [251, 551, 5, 25]
    left_horizontal_box_bottom = [181, 571, 75, 5]
    right_horizontal_box_top = [352, 551, 75, 5]
    right_horizontal_box_left = [352, 551, 5, 25]
    right_horizontal_box_right = [422, 551, 5, 25]
    right_horizontal_box_bottom = [352, 571, 75, 5]
    left_upside_down_l_top = [88, 551, 58, 5]
    left_upside_down_l_right = [141, 551, 5, 90]
    left_upside_down_l_upper_left = [88, 551, 5, 25]
    left_upside_down_l_left_horizontal = [88, 571, 42, 5]
    left_upside_down_l_lower_left = [125, 571, 5, 70]
    left_upside_down_l_bottom = [125, 636, 20, 5]
    right_upside_down_l_top = [465, 551, 58, 5]
    right_upside_down_l_left = [465, 551, 5, 90]
    right_upside_down_l_upper_right = [518, 551, 5, 25]
    right_upside_down_l_right_horizontal = [481, 571, 37, 5]
    right_upside_down_l_lower_right = [481, 571, 5, 70]
    right_upside_down_l_bottom = [465, 636, 20, 5]
    left_wall_box_top = [44, 619, 45, 5]
    left_wall_box_right = [84, 619, 5, 25]
    left_wall_box_bottom = [44, 639, 45, 5]
    right_wall_box_top = [519, 619, 45, 5]
    right_wall_box_left = [519, 619, 5, 25]
    right_wall_box_bottom = [519, 639, 45, 5]
    left_upside_down_t_top = [181, 629, 20, 5]
    left_upside_down_t_upper_left = [181, 629, 5, 70]
    left_upside_down_t_left_horizontal = [86, 694, 95, 5]
    left_upside_down_t_lower_left = [86, 694, 5, 25]
    left_upside_down_t_upper_right = [196, 629, 5, 70]
    left_upside_down_t_right_horizontal = [196, 694, 60, 5]
    left_upside_down_t_lower_right = [251, 694, 5, 25]
    left_upside_down_t_bottom = [86, 714, 170, 5]
    right_upside_down_t_top = [407, 629, 16, 5]
    right_upside_down_t_upper_left = [407, 629, 5, 70]
    right_upside_down_t_left_horizontal = [352, 694, 60, 5]
    right_upside_down_t_lower_left = [352, 694, 5, 25]
    right_upside_down_t_upper_right = [422, 629, 5, 70]
    right_upside_down_t_right_horizontal = [424, 694, 96, 5]
    right_upside_down_t_lower_right = [517, 694, 5, 25]
    right_upside_down_t_bottom = [352, 714, 170, 5]
    ghost_cage_horizontal_left = [237, 352, 44, 8]
    ghost_cage_horizontal_right = [322, 352, 44, 8]
    ghost_cage_vertical_left = [237, 352, 8, 88]
    ghost_cage_vertical_right = [358, 352, 8, 88]
    ghost_cage_bottom = [237, 432, 128, 8]

    wall_map = [top_row, upper_box_left, upper_box_right, upper_box_bottom,
                top_left_vertical, top_right_vertical, top_left_lower, top_right_lower,
                upper_mid_left_vertical, upper_mid_right_vertical, upper_mid_right_lower,
                upper_mid_left_lower, lower_mid_left_lower, lower_mid_left_top, lower_mid_left_vertical,
                lower_mid_right_lower, lower_mid_right_top, lower_mid_right_vertical, bottom_left_vertical,
                bottom_right_vertical, bottom_row, top_left_medium_box_bottom, top_left_medium_box_left,
                top_left_medium_box_right, top_left_medium_box_top, top_right_medium_box_bottom,
                top_right_medium_box_left, top_right_medium_box_right, top_right_medium_box_top,
                top_left_small_box_bottom, top_left_small_box_left, top_left_small_box_right,
                top_left_small_box_top, top_right_small_box_bottom, top_right_small_box_left,
                top_right_small_box_right, top_right_small_box_top, top_left_large_box_bottom,
                top_left_large_box_left, top_left_large_box_right, top_left_large_box_top,
                top_right_large_box_bottom, top_right_large_box_left, top_right_large_box_right,
                top_right_large_box_top, upper_middle_t_bottom, upper_middle_t_bottom_left,
                upper_middle_t_bottom_right, upper_middle_t_top, upper_middle_t_top_left,
                upper_middle_t_top_right, upper_middle_t_upper_left_bottom, upper_middle_t_upper_right_bottom,
                left_t_bottom, left_t_left_vertical, left_t_right_lower_horizontal, left_t_right_lower_vertical,
                left_t_right_upper_horizontal, left_t_right_upper_vertical, left_t_right_vertical, left_t_top,
                right_t_bottom, right_t_left_lower_horizontal, right_t_left_lower_vertical,
                right_t_left_upper_horizontal,
                right_t_left_upper_vertical, right_t_left_vertical, right_t_right_vertical, right_t_top,
                left_vertical_box_bottom, left_vertical_box_left, left_vertical_box_right, left_vertical_box_top,
                right_vertical_box_bottom, right_vertical_box_left, right_vertical_box_right, right_vertical_box_top,
                lower_middle_t_bottom, lower_middle_t_left_horizontal, lower_middle_t_lower_left,
                lower_middle_t_lower_right,
                lower_middle_t_right_horizontal, lower_middle_t_top, lower_middle_t_upper_left,
                lower_middle_t_upper_right,
                bottom_middle_t_bottom, bottom_middle_t_left_horizontal, bottom_middle_t_lower_left,
                bottom_middle_t_lower_right,
                bottom_middle_t_right_horizontal, bottom_middle_t_top, bottom_middle_t_upper_left,
                bottom_middle_t_upper_right,
                left_horizontal_box_bottom, left_horizontal_box_left, left_horizontal_box_right,
                left_horizontal_box_top,
                right_horizontal_box_bottom, right_horizontal_box_left, right_horizontal_box_right,
                right_horizontal_box_top,
                left_upside_down_l_bottom, left_upside_down_l_left_horizontal, left_upside_down_l_lower_left,
                left_upside_down_l_right,
                left_upside_down_l_top, left_upside_down_l_upper_left, right_upside_down_l_bottom,
                right_upside_down_l_left,
                right_upside_down_l_lower_right, right_upside_down_l_right_horizontal, right_upside_down_l_top,
                right_upside_down_l_upper_right,
                left_wall_box_bottom, left_wall_box_right, left_wall_box_top, right_wall_box_bottom,
                right_wall_box_left, right_wall_box_top,
                left_upside_down_t_bottom, left_upside_down_t_left_horizontal, left_upside_down_t_lower_left,
                left_upside_down_t_lower_right,
                left_upside_down_t_right_horizontal, left_upside_down_t_top, left_upside_down_t_upper_left,
                left_upside_down_t_upper_right,
                right_upside_down_t_bottom, right_upside_down_t_left_horizontal, right_upside_down_t_lower_left,
                right_upside_down_t_lower_right,
                right_upside_down_t_right_horizontal, right_upside_down_t_top, right_upside_down_t_upper_left,
                right_upside_down_t_upper_right,
                ghost_cage_bottom, ghost_cage_horizontal_left, ghost_cage_horizontal_right, ghost_cage_vertical_left,
                ghost_cage_vertical_right]

    # Like pellets, takes each element from the walls list 
    # creates a wall object
    # and adds the wall to the wall list and sprite list
    for walls in wall_map:
        wall = Wall(walls[0], walls[1], walls[2], walls[3])
        wall_list.add(wall)

    return wall_list


def gameover():
    font = pygame.font.SysFont('comicsansms', 20, True, False)
    lose_font = pygame.font.SysFont('comicsansm', 25, True, False)
    lose_text = lose_font.render("Game Over!", True, (255, 255, 255))
    gameover_text = font.render("Play again? (Y/N)", True, (255, 255, 255))

    screen.blit(lose_text, (248, 330))
    screen.blit(gameover_text, (248, 355))

    death_music = pygame.mixer.Sound('audio/pacman_death.ogg')
    death_music.set_volume(0.25)
    death_music.play()

    pygame.display.update()

    while True:
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                death_music.stop()
                game()
                break
            elif event.key == pygame.K_n:
                exit()


# initialize pygame
pygame.init()

# Set screen size
screen = pygame.display.set_mode((600, 800))

# Hide the mouse since it is not needed
pygame.mouse.set_visible(False)

clock = pygame.time.Clock()

# Runs main program
menu()
