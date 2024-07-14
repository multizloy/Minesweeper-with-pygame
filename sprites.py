import random
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

        boardSurface.blit(self.image, (self.x, self.y))
        # boardSurface.blit(tileUnknown, (self.x, self.y))

    def __repr__(self):
        return self.type


class Board:
    def __init__(self):
        self.boardSurface = pygame.Surface((WIDTH, HEIGHT))
        self.boardList = [
            [Tile(col, row, tileEmpty, ".") for row in range(ROWS)]
            for col in range(COLS)
        ]
        self.placeMines()

    def placeMines(self):
        for _ in range(AMOUNT_MINES):
            while True:
                x = random.randint(0, ROWS - 1)
                y = random.randint(0, COLS - 1)

                if self.boardList[x][y].type == ".":
                    self.boardList[x][y].image = tileMine
                    self.boardList[x][y].type = "X"
                    break

    def placeClues(self):
        pass

    @staticmethod
    def isInside(x, y):
        return 0 <= x < ROWS and 0 <= y < COLS

    # проверяем соседние кнопки\тайлы\клетки
    def checkNeighbors(self, x, y):
        totalMines = 0
        for xOffset in range(-1, 2):
            for yOffset in range(-1, 2):
                xNeighbor = x + xOffset
                yNeighbor = y + yOffset
                if (
                    self.isInside(xNeighbor, yNeighbor)
                    and self.boardList[xNeighbor][yNeighbor].type == "X"
                ):
                    totalMines += 1
        return totalMines

    def draw(self, screen):
        for row in self.boardList:
            for tile in row:
                tile.draw(self.boardSurface)
        screen.blit(self.boardSurface, (0, 0))

    def displayBoard(self):
        for row in self.boardList:
            print(row)
