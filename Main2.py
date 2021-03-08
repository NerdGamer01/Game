from math import sqrt
import numpy as np
import pygame

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Chess')

# Size of the squares
s = 80

# Upper left corner of chess board
o = (0,0)

# Sets up the window
screen = pygame.display.set_mode([s * 8, s * 8])

# Variable which detemines which window is used (0: main menu, 1: game, 2: pause menu)
window = 1

# Variable is True if player clicked in that iteration of game loop, otherwise False
clicked = False

a = int("0000000000000000000000000000000000000000000000001111111100000000", 2)
print(a)
a = a << 2
print(a)
print(str(bin(a)))
#Load image file for Chess Pieces
Img = pygame.image.load('chess pieces.png')
Img = pygame.transform.scale(Img, (s * 6,s * 2))

class Pieces(pygame.sprite.Sprite):
    def __init__(self, type, white, x, y):
        # List pieces in order they are occur in the image
        piece_types = ['king', 'queen', 'bishop', 'knight', 'rook', 'pawn']
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        self.white = white
        self.tile = (x, y)

        # Creates image for this piece
        self.image = pygame.Surface((s, s), pygame.SRCALPHA, 32)
        self.image = self.image.convert_alpha()

        if white:
            self.image.blit(Img, (0, 0), (s * piece_types.index(type), 0, s, s))
        else:
            self.image.blit(Img, (0, 0), (s * piece_types.index(type), s, s, s))

        # Sets the pieces intial position
        self.rect = self.image.get_rect()
        self.rect.topleft = ((s * x) + o[0], (s * y) + o[0])

class Board:
    def __init__(self):
        self.white_pieces = dict()
        self.black_pieces = dict()
        self.spots = dict()
        self.sprites = pygame.sprite.Group()
        self.white_turn = True

        for key in ['king', 'queen', 'bishop', 'knight', 'rook', 'pawn']:
            self.white_pieces[key] = []
            self.black_pieces[key] = []

        # Peaces listed in the order they are at the start of the game
        piece_order = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']

        # Creates Pieces
        for i in range(8):
            p = piece_order[i]
            self.white_pieces[p].append(Pieces( p, True, i, 7))
            self.black_pieces[p].append(Pieces( p, False, i, 0))
            self.white_pieces['pawn'].append(Pieces( 'pawn', True, i, 6))
            self.black_pieces['pawn'].append(Pieces( 'pawn', False, i, 1))

            self.spots[(i,7)] = self.white_pieces[p][-1]
            self.spots[(i,6)] = self.white_pieces['pawn'][-1]
            self.spots[(i, 0)] = self.black_pieces[p][-1]
            self.spots[(i, 1)] = self.black_pieces['pawn'][-1]

            self.sprites.add(self.white_pieces[p][-1])
            self.sprites.add(self.white_pieces['pawn'][-1])
            self.sprites.add(self.black_pieces[p][-1])
            self.sprites.add(self.black_pieces['pawn'][-1])

    def draw(self):
        global screen
        # Draws chessboard pattern
        xs = s
        ys = 0
        while ys < s * 8:
            if xs <= s * 7:
                if xs >= o[0]:
                    pygame.draw.rect(screen, (125, 25, 10), (xs + o[0], ys + o[1], s, s))
                xs += s * 2
            else:
                xs -= s * 9
                ys += s

        self.sprites.draw(screen)

    def generate_legal_moves(self):
        pass

    def update(self):
        pass

# Game loop
running = True
while running:
    board = Board()
    # Check user input
    for event in pygame.event.get():

        # Check if player clicked
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            clicked = True

        # Cecks if user closed the window
        elif event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    if window == 1:
        board.draw()

    pygame.display.flip()
    clock.tick(30)
    clicked = False