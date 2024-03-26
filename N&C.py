import random as rd
import pygame as pg
import sys

pg.init()
pg.mixer.init()

width, height = 600, 600
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Naughts & Crosses")

main_bg = pg.image.load("assets/images/title.png")
select_bg = pg.image.load("assets/images/select_screen.png")
base_bg = pg.image.load("assets/images/base.jpg")
tie_bg = pg.image.load("assets/images/tie.png")
cross_win_img = pg.image.load("assets/images/crosses_win.png")
naught_win = pg.image.load("assets/images/naughts_win.png")
cross_img = pg.image.load("assets/images/cross.png")
naught_img = pg.image.load("assets/images/naught.png")

CHALK_SOUNDS = ["assets/audio/chalk1.mp3", "assets/audio/chalk2.mp3",
                "assets/audio/chalk3.mp3", "assets/audio/chalk4.mp3"]
cymbal_sfx = pg.mixer.Sound("assets/audio/cymbal.mp3")

square_1_x_y = (25, 25)
square_2_x_y = (225, 25)
square_3_x_y = (425, 25)
square_4_x_y = (25, 225)
square_5_x_y = (225, 225)
square_6_x_y = (425, 225)
square_7_x_y = (25, 425)
square_8_x_y = (225, 425)
square_9_x_y = (425, 425)

square_1_button_rect = pg.Rect(0, 0, 200, 200)
square_2_button_rect = pg.Rect(200, 0, 200, 200)
square_3_button_rect = pg.Rect(400, 0, 200, 200)

square_4_button_rect = pg.Rect(0, 200, 200, 200)
square_5_button_rect = pg.Rect(200, 200, 200, 200)
square_6_button_rect = pg.Rect(400, 200, 200, 200)

square_7_button_rect = pg.Rect(0, 400, 200, 600)
square_8_button_rect = pg.Rect(200, 400, 200, 200)
square_9_button_rect = pg.Rect(400, 400, 200, 200)


class Player:
    def __init__(self):
        self.wins = 0
        self.choice = ""
        self.cpu = ""
        self.grid = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.cpu_img = naught_img

    def computer_choice(self):
        while True:
            choice = rd.randrange(0, 9)  # Use 9 to include the last square
            if self.grid[choice] == 0:
                self.grid[choice] = self.cpu
                if choice == 0:
                    screen.blit(self.cpu_img, square_1_x_y)
                elif choice == 1:
                    screen.blit(self.cpu_img, square_2_x_y)
                elif choice == 2:
                    screen.blit(self.cpu_img, square_3_x_y)
                elif choice == 3:
                    screen.blit(self.cpu_img, square_4_x_y)
                elif choice == 4:
                    screen.blit(self.cpu_img, square_5_x_y)
                elif choice == 5:
                    screen.blit(self.cpu_img, square_6_x_y)
                elif choice == 6:
                    screen.blit(self.cpu_img, square_7_x_y)
                elif choice == 7:
                    screen.blit(self.cpu_img, square_8_x_y)
                elif choice == 8:
                    screen.blit(self.cpu_img, square_9_x_y)
                pg.display.flip()
                break

    def check_win_x(self):
        for row in range(0, 9, 3):
            if self.grid[row] == self.grid[row + 1] == self.grid[row + 2] == 'x':
                return True
        for col in range(3):
            if self.grid[col] == self.grid[col + 3] == self.grid[col + 6] == 'x':
                return True
        if self.grid[0] == self.grid[4] == self.grid[8] != 0 or self.grid[2] == self.grid[4] == self.grid[6] == 'x':
            return True

        return False

    def check_win_o(self):
        for row in range(0, 9, 3):
            if self.grid[row] == self.grid[row + 1] == self.grid[row + 2] == 'o':
                return True
        for col in range(3):
            if self.grid[col] == self.grid[col + 3] == self.grid[col + 6] == 'o':
                return True
        if self.grid[0] == self.grid[4] == self.grid[8] != 0 or self.grid[2] == self.grid[4] == self.grid[6] == 'o':
            return True

        return False



def game_loop():
    player1 = Player()
    at_main_menu = True
    at_select_menu = False
    at_crosses_win = False
    at_naughts_win = False
    at_tie = False
    run = True

    while run:
        pg.mixer.music.load("assets/audio/schoolyard bgm.mp3")
        pg.mixer.music.play(loops=-1)
        while at_main_menu:
            screen.blit(main_bg, (0, 0))
            pg.display.flip()
            while at_main_menu:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                        sys.exit()
                    if event.type == pg.MOUSEBUTTONDOWN:
                        chalk_sound = rd.choice(CHALK_SOUNDS)
                        pg.mixer.Sound(chalk_sound).play()
                        at_main_menu = False
                        at_select_menu = True
        while at_select_menu:
            screen.blit(select_bg, (0, 0))
            pg.display.flip()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if mouse_y < height / 2:
                        player1.choice = "o"
                        player1.cpu = "x"
                        chalk_sound = rd.choice(CHALK_SOUNDS)
                        pg.mixer.Sound(chalk_sound).play()
                        at_select_menu = False
                        at_game = True
                        screen.blit(base_bg, (0, 0))
                        player1.cpu_img = cross_img
                        player1.computer_choice()
                    else:
                        player1.choice = "x"
                        player1.cpu = "o"
                        chalk_sound = rd.choice(CHALK_SOUNDS)
                        pg.mixer.Sound(chalk_sound).play()
                        at_select_menu = False
                        at_game = True
                        screen.blit(base_bg, (0, 0))
                        player1.cpu_img = naught_img

        while at_game and player1.choice == "x":
            pg.display.flip()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if player1.check_win_o():
                    at_game = False
                    at_naughts_win = True
                if player1.check_win_x():
                    at_game = False
                    at_crosses_win = True
                if event.type == pg.MOUSEBUTTONDOWN:
                    if 0 not in player1.grid:
                        at_game = False
                        at_tie = True
                    if square_1_button_rect.collidepoint(event.pos) and player1.grid[0] == 0:
                        screen.blit(cross_img, square_1_x_y)
                        player1.grid[0] = "x"
                        chalk_sound = rd.choice(CHALK_SOUNDS)
                        pg.mixer.Sound(chalk_sound).play()
                        if player1.check_win_x():
                            at_game = False
                            at_crosses_win = True
                        if 0 in player1.grid:
                            player1.computer_choice()
                            if player1.check_win_o():
                                at_game = False
                                at_naughts_win = True

                    if square_2_button_rect.collidepoint(event.pos) and player1.grid[1] == 0:
                        screen.blit(cross_img, square_2_x_y)
                        player1.grid[1] = "x"
                        chalk_sound = rd.choice(CHALK_SOUNDS)
                        pg.mixer.Sound(chalk_sound).play()
                        if player1.check_win_x():
                            at_game = False
                            at_crosses_win = True
                        if 0 in player1.grid:
                            player1.computer_choice()
                            if player1.check_win_o():
                                at_game = False
                                at_naughts_win = True

                    if square_3_button_rect.collidepoint(event.pos) and player1.grid[2] == 0:
                        screen.blit(cross_img, square_3_x_y)
                        player1.grid[2] = "x"
                        chalk_sound = rd.choice(CHALK_SOUNDS)
                        pg.mixer.Sound(chalk_sound).play()
                        if player1.check_win_x():
                            at_game = False
                            at_crosses_win = True
                        if 0 in player1.grid:
                            player1.computer_choice()
                            if player1.check_win_o():
                                at_game = False
                                at_naughts_win = True

                    if square_4_button_rect.collidepoint(event.pos) and player1.grid[3] == 0:
                        screen.blit(cross_img, square_4_x_y)
                        player1.grid[3] = "x"
                        chalk_sound = rd.choice(CHALK_SOUNDS)
                        pg.mixer.Sound(chalk_sound).play()
                        if player1.check_win_x():
                            at_game = False
                            at_crosses_win = True
                        if 0 in player1.grid:
                            player1.computer_choice()
                            if player1.check_win_o():
                                at_game = False
                                at_naughts_win = True

                    if square_5_button_rect.collidepoint(event.pos) and player1.grid[4] == 0:
                        screen.blit(cross_img, square_5_x_y)
                        player1.grid[4] = "x"
                        chalk_sound = rd.choice(CHALK_SOUNDS)
                        pg.mixer.Sound(chalk_sound).play()
                        if player1.check_win_x():
                            at_game = False
                            at_crosses_win = True
                        if 0 in player1.grid:
                            player1.computer_choice()
                            if player1.check_win_o():
                                at_game = False
                                at_naughts_win = True

                    if square_6_button_rect.collidepoint(event.pos) and player1.grid[5] == 0:
                        screen.blit(cross_img, square_6_x_y)
                        player1.grid[5] = "x"
                        chalk_sound = rd.choice(CHALK_SOUNDS)
                        pg.mixer.Sound(chalk_sound).play()
                        if player1.check_win_x():
                            at_game = False
                            at_crosses_win = True
                        if 0 in player1.grid:
                            player1.computer_choice()
                            if player1.check_win_o():
                                at_game = False
                                at_naughts_win = True

                    if square_7_button_rect.collidepoint(event.pos) and player1.grid[6] == 0:
                        screen.blit(cross_img, square_7_x_y)
                        player1.grid[6] = "x"
                        chalk_sound = rd.choice(CHALK_SOUNDS)
                        pg.mixer.Sound(chalk_sound).play()
                        if player1.check_win_x():
                            at_game = False
                            at_crosses_win = True
                        if 0 in player1.grid:
                            player1.computer_choice()
                            if player1.check_win_o():
                                at_game = False
                                at_naughts_win = True

                    if square_8_button_rect.collidepoint(event.pos) and player1.grid[7] == 0:
                        screen.blit(cross_img, square_8_x_y)
                        player1.grid[7] = "x"
                        chalk_sound = rd.choice(CHALK_SOUNDS)
                        pg.mixer.Sound(chalk_sound).play()
                        if player1.check_win_x():
                            at_game = False
                            at_crosses_win = True
                        if 0 in player1.grid:
                            player1.computer_choice()
                            if player1.check_win_o():
                                at_game = False
                                at_naughts_win = True

                    if square_9_button_rect.collidepoint(event.pos) and player1.grid[8] == 0:
                        screen.blit(cross_img, square_9_x_y)
                        player1.grid[8] = "x"
                        chalk_sound = rd.choice(CHALK_SOUNDS)
                        pg.mixer.Sound(chalk_sound).play()
                        if player1.check_win_x():
                            at_game = False
                            at_crosses_win = True
                        if 0 in player1.grid:
                            player1.computer_choice()
                            if player1.check_win_o():
                                at_game = False
                                at_naughts_win = True

        while at_game and player1.choice == "o":
            pg.display.flip()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if 0 not in player1.grid:
                        at_game = False
                        at_tie = True
                    if square_1_button_rect.collidepoint(event.pos) and player1.grid[0] == 0:
                        screen.blit(naught_img, square_1_x_y)
                        player1.grid[0] = "o"
                        chalk_sound = rd.choice(CHALK_SOUNDS)
                        pg.mixer.Sound(chalk_sound).play()
                        if player1.check_win_o():
                            at_game = False
                            at_naughts_win = True
                        if 0 in player1.grid:
                            player1.computer_choice()
                            if player1.check_win_x():
                                at_game = False
                                at_crosses_win = True

                    if square_2_button_rect.collidepoint(event.pos) and player1.grid[1] == 0:
                        screen.blit(naught_img, square_2_x_y)
                        player1.grid[1] = "o"
                        chalk_sound = rd.choice(CHALK_SOUNDS)
                        pg.mixer.Sound(chalk_sound).play()
                        if player1.check_win_o():
                            at_game = False
                            at_naughts_win = True
                        if 0 in player1.grid:
                            player1.computer_choice()
                            if player1.check_win_x():
                                at_game = False
                                at_crosses_win = True

                    if square_3_button_rect.collidepoint(event.pos) and player1.grid[2] == 0:
                        screen.blit(naught_img, square_3_x_y)
                        player1.grid[2] = "o"
                        chalk_sound = rd.choice(CHALK_SOUNDS)
                        pg.mixer.Sound(chalk_sound).play()
                        if player1.check_win_o():
                            at_game = False
                            at_naughts_win = True
                        if 0 in player1.grid:
                            player1.computer_choice()
                            if player1.check_win_x():
                                at_game = False
                                at_crosses_win = True

                    if square_4_button_rect.collidepoint(event.pos) and player1.grid[3] == 0:
                        screen.blit(naught_img, square_4_x_y)
                        player1.grid[3] = "o"
                        chalk_sound = rd.choice(CHALK_SOUNDS)
                        pg.mixer.Sound(chalk_sound).play()
                        if player1.check_win_o():
                            at_game = False
                            at_naughts_win = True
                        if 0 in player1.grid:
                            player1.computer_choice()
                            if player1.check_win_x():
                                at_game = False
                                at_crosses_win = True

                    if square_5_button_rect.collidepoint(event.pos) and player1.grid[4] == 0:
                        screen.blit(naught_img, square_5_x_y)
                        player1.grid[4] = "o"
                        chalk_sound = rd.choice(CHALK_SOUNDS)
                        pg.mixer.Sound(chalk_sound).play()
                        if player1.check_win_o():
                            at_game = False
                            at_naughts_win = True
                        if 0 in player1.grid:
                            player1.computer_choice()
                            if player1.check_win_x():
                                at_game = False
                                at_crosses_win = True

                    if square_6_button_rect.collidepoint(event.pos) and player1.grid[5] == 0:
                        screen.blit(naught_img, square_6_x_y)
                        player1.grid[5] = "o"
                        chalk_sound = rd.choice(CHALK_SOUNDS)
                        pg.mixer.Sound(chalk_sound).play()
                        if player1.check_win_o():
                            at_game = False
                            at_naughts_win = True
                        if 0 in player1.grid:
                            player1.computer_choice()
                            if player1.check_win_x():
                                at_game = False
                                at_crosses_win = True

                    if square_7_button_rect.collidepoint(event.pos) and player1.grid[6] == 0:
                        screen.blit(naught_img, square_7_x_y)
                        player1.grid[6] = "o"
                        chalk_sound = rd.choice(CHALK_SOUNDS)
                        pg.mixer.Sound(chalk_sound).play()
                        if player1.check_win_o():
                            at_game = False
                            at_naughts_win = True
                        if 0 in player1.grid:
                            player1.computer_choice()
                            if player1.check_win_x():
                                at_game = False
                                at_crosses_win = True

                    if square_8_button_rect.collidepoint(event.pos) and player1.grid[7] == 0:
                        screen.blit(naught_img, square_8_x_y)
                        player1.grid[7] = "o"
                        chalk_sound = rd.choice(CHALK_SOUNDS)
                        pg.mixer.Sound(chalk_sound).play()
                        if player1.check_win_o():
                            at_game = False
                            at_naughts_win = True
                        if 0 in player1.grid:
                            player1.computer_choice()
                            if player1.check_win_x():
                                at_game = False
                                at_crosses_win = True

                    if square_9_button_rect.collidepoint(event.pos) and player1.grid[8] == 0:
                        screen.blit(naught_img, square_9_x_y)
                        player1.grid[8] = "o"
                        chalk_sound = rd.choice(CHALK_SOUNDS)
                        pg.mixer.Sound(chalk_sound).play()
                        if player1.check_win_o():
                            at_game = False
                            at_naughts_win = True
                        if 0 in player1.grid:
                            player1.computer_choice()
                            if player1.check_win_x():
                                at_game = False
                                at_crosses_win = True

        while at_crosses_win:
            screen.blit(cross_win_img, (0, 0))
            pg.display.flip()
            player1.grid = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    chalk_sound = rd.choice(CHALK_SOUNDS)
                    pg.mixer.Sound(chalk_sound).play()
                    at_main_menu = True
                    at_crosses_win = False

        while at_naughts_win:
            screen.blit(naught_win, (0, 0))
            pg.display.flip()
            player1.grid = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    chalk_sound = rd.choice(CHALK_SOUNDS)
                    pg.mixer.Sound(chalk_sound).play()
                    at_main_menu = True
                    at_naughts_win = False

        while at_tie:
            screen.blit(tie_bg, (0, 0))
            pg.display.flip()
            player1.grid = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    chalk_sound = rd.choice(CHALK_SOUNDS)
                    pg.mixer.Sound(chalk_sound).play()
                    at_main_menu = True
                    at_tie = False



chalk_sound = rd.choice(CHALK_SOUNDS)
pg.mixer.Sound(chalk_sound).play()

game_loop()
