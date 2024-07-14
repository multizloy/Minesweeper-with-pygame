import pygame
import os

# Colors

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
DARKGREEN = (0, 200, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BGCOLOUR = DARKGREY

# SETTINGS for game
TILESIZE = 32
ROWS = 15
COLS = 15
AMOUNT_MINES = 40
WIDTH = TILESIZE * ROWS
HEIGHT = TILESIZE * COLS
FPS = 60
TITLE = "Minesweeper Clone"

# вытаскиваем картинки
tileNumber = []
for i in range(1, 9):
    tileNumber.append(
        pygame.transform.scale(
            pygame.image.load(os.path.join("assets", f"Tile{i}.png")),
            (TILESIZE, TILESIZE),
        )
    )

tileEmpty = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "TileEmpty.png")), (TILESIZE, TILESIZE)
)
tileExploded = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "TileExploded.png")), (TILESIZE, TILESIZE)
)
tileFlag = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "TileFlag.png")), (TILESIZE, TILESIZE)
)
tileMine = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "TileMine.png")), (TILESIZE, TILESIZE)
)
tileNotMine = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "TileNotMine.png")), (TILESIZE, TILESIZE)
)
tileUnknown = pygame.transform.scale(
    pygame.image.load(os.path.join("assets", "TileUnknown.png")), (TILESIZE, TILESIZE)
)
