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
        if not self.flagged and self.revealed:
            boardSurface.blit(self.image, (self.x, self.y))
        elif self.flagged and not self.revealed:
            boardSurface.blit(tileFlag, (self.x, self.y))
        elif not self.revealed:
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
        self.placeMines()
        self.placeClues()
        self.dug = []

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
        for x in range(ROWS):
            for y in range(COLS):
                if self.boardList[x][y].type != "X":
                    totalMines = self.checkNeighbors(x, y)
                    if totalMines > 0:
                        self.boardList[x][y].image = tileNumber[totalMines - 1]
                        self.boardList[x][y].type = "C"

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

    def dig(self, x, y):
        self.dug.append((x, y))
        if self.boardList[x][y].type == "X":
            self.boardList[x][y].revealed = True
            self.boardList[x][y].image = tileExploded
            return False
        elif self.boardList[x][y].type == "C":
            self.boardList[x][y].revealed = True
            return True

        self.boardList[x][y].revealed = True

        for row in range(max(0, x - 1), min(ROWS - 1, x + 1) + 1):
            for col in range(max(0, y - 1), min(COLS - 1, y + 1) + 1):
                if (row, col) not in self.dug:
                    self.dig(row, col)
        return True

    def displayBoard(self):
        for row in self.boardList:
            print(row)
