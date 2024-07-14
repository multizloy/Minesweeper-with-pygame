import pygame
from settings import *

# types list
""" 
    . = unknown
    X = mine
    C =  clue
    / = empty
"""


class Tile:
    def __init__(self, x, y, image, type, revealed=False, flagged=False):
        self.x, self.y = x * TILESIZE, y * TILESIZE
        self.image = image
        self.type = type
        self.revealed = revealed
        self.flagged = flagged

    def draw(self, boardSurface):
        boardSurface.blit(tileUnknown, (self.x, self.y))

    def __repr__(self):
        return self.type


class Board:
    def __init__(self):
        self.boardSurface = pygame.Surface((WIDTH, HEIGHT))
        self.boardList = [
            [Tile(col, row, tileEmpty, ".") for row in range(ROWS)]
            for col in range(COLS)
        ]

    def draw(self, screen):
        for row in self.boardList:
            for tile in row:
                tile.draw(self.boardSurface)
        screen.blit(self.boardSurface, (0, 0))

    def displayBoard(self):
        for row in self.boardList:
            print(row)
