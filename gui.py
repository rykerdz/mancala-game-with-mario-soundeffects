import pygame
from sys import exit
import math
from time import sleep
from PIL import Image, ImageFilter




WINDOW_SIZE = (1080, 720)
BOARD_COLOR = (164, 116, 73)
BOARD_SIZE = (900, 400)
BORDER_COLOR = (78,53,36)
FOSS_COLOR = (142, 86, 46)

class GameUI:
    foss = ''
    turn = 1
    step_1 = True
    coords = (0, 0)

    def __init__(self, play):
        pygame.mixer.init()
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('assets/audio/Super Mario Bros. medley.mp3'), -1)

        self.play = play
        pygame.init()
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("Mancala game")
        self.load_assets()
        FPS = 60
        clock = pygame.time.Clock()
        while(True):
            clock.tick(FPS)
            self.screen.blit(self.bg, (0, 0))
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.coords = pygame.mouse.get_pos()

    def load_assets(self):
        self.bg = pygame.image.load("assets/images/background.jpg")
        self.menu_font = pygame.font.Font("assets/fonts/baron-kuffner.regular.otf", 180)
        self.numbers_font = pygame.font.Font("assets/fonts/baron-kuffner.regular.otf", 70)




    def draw(self):
        
        # Board
        pygame.draw.rect(self.screen, BORDER_COLOR, pygame.Rect(70, 235, 930, 380), border_radius=200)
        pygame.draw.rect(self.screen, BOARD_COLOR, pygame.Rect(85, 250, 900, 350), border_radius=200)

        # Logo
        self.screen.blit(self.menu_font.render("MANCALA", 0, BORDER_COLOR), (270, 0))

        # Fosses ta3 pc
        for i in range(6):
            pygame.draw.circle(self.screen, FOSS_COLOR, (260+(i*110), 320), 45, 8)
            self.screen.blit(self.numbers_font.render(str(self.play.game.state.board[self.play.game.state.dict[2][i]]), 0, FOSS_COLOR), (235+(i*110), 262))


        # computer magazine
        pygame.draw.rect(self.screen, FOSS_COLOR, pygame.Rect(120, 360, 90, 130), 8, border_radius=30)
        self.screen.blit(self.numbers_font.render(str(self.play.game.state.board['2']), 0, FOSS_COLOR), (140, 365))

        # posses te3 player
        for i in range(6):
            pygame.draw.circle(self.screen, BORDER_COLOR, (260+(i*110), 530), 45, 8)
            self.screen.blit(self.numbers_font.render(str(self.play.game.state.board[self.play.game.state.dict[1][i]]), 0, BORDER_COLOR), (235+(i*110), 470))

         # player's magazine
        pygame.draw.rect(self.screen, BORDER_COLOR, pygame.Rect(865, 360, 90, 130), 8, border_radius=30)
        self.screen.blit(self.numbers_font.render(str(self.play.game.state.board['1']), 0, BORDER_COLOR), (885, 365))

        if self.play.game.game_over():
            winner = self.play.game.find_winner()
            self.turn = "YOU WON!" if winner == self.play.game.player_side else "YOU LOST!"

        if self.turn == 1:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            possible_moves = self.play.game.state.possible_moves(1)
            coords_list = [260, 370, 480, 590, 700, 810]
            sqy = (y - 530)**2
            for i in range(len(coords_list)):
                sqx = (x - coords_list[i])**2
                if math.sqrt(sqx + sqy) < 45:
                    if self.play.game.state.dict[1][i] in possible_moves:
                        pygame.draw.circle(self.screen, FOSS_COLOR, (260+(i*110), 530), 45, 8)
                        self.screen.blit(self.numbers_font.render(str(self.play.game.state.board[self.play.game.state.dict[1][i]]), 0, FOSS_COLOR), (235+(i*110), 470))

            for i in range(len(coords_list)):
                sqy = (self.coords[1] - 530)**2
                sqx = (self.coords[0] - coords_list[i])**2
                if math.sqrt(sqx + sqy) < 45:
                    if self.play.game.state.dict[1][i] in possible_moves:
                        self.turn = self.play.human_turn(self.play.game.state.dict[1][i])
                        pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/audio/smb_coin.wav'))
            self.coords = (0, 0)

        elif self.turn == 2:
            if self.step_1:
                self.foss = self.play.computer_turn()
                i = ord(self.foss) - 65 - 6
                pygame.draw.circle(self.screen, BORDER_COLOR, (260+(i*110), 320), 45, 8)
                self.screen.blit(self.numbers_font.render(str(self.play.game.state.board[self.play.game.state.dict[2][i]]), 0, BORDER_COLOR), (235+(i*110), 262))
                self.step_1 = False
                pygame.display.update()
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/audio/smb_jump-small.wav'))
                sleep(2)
            else:
                self.turn = self.play.game.state.do_move(self.foss, 2)
                self.step_1 = True
        else:
            pygame.image.save(self.screen, "screenshot2.jpg")
            im = Image.open(r"screenshot2.jpg")

            # Blurring the image
            im1 = im.filter(ImageFilter.GaussianBlur(4))

            bg_im = self.pilImageToSurface(im1)
            self.screen.blit(bg_im, (0, 0))

            self.screen.blit(self.menu_font.render(self.turn, 0, BORDER_COLOR), (250, 200))
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('assets/audio/smb_mariodie.wav'))
            pygame.display.update()
            sleep(5)


        pygame.display.update()
        
    def pilImageToSurface(self, pilImage):
        return pygame.image.fromstring(
            pilImage.tobytes(), pilImage.size, pilImage.mode).convert()
        

        
