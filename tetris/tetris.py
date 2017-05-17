import pygame
import random
import time

#Define some colors
#                R    G    B
WHITE       = (255, 255, 255)
GRAY        = (185, 185, 185)
BLACK       = (  0,   0,   0)
RED         = (155,   0,   0)
GREEN       = (  0, 155,   0)
BLUE        = (  0,   0, 155)
YELLOW      = (155, 155,   0)

#Call this function so the Pygame library can initialize itself
pygame.init()

#Create an 800*600 sized screen
screen = pygame.display.set_mode([800, 600])

#This sets the name of the window
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

#보드 색깔
BORDERCOLOR = BLUE
#블럭 색깔
BLOCKCOLORS = (BLUE,GREEN,RED,YELLOW)

#Piece array 크기
PIECEWIDTH = 5
PIECEHEIGHT = 5

Piece1 = [['.....',
           '.....',
           '..OO.',
           '.OO..',
           '.....'],
         ['.....',
          '..O..',
          '..OO.',
          '...O.',
          '.....']]

Piece2 = [['.....',
           '.....',
           '.OO..',
           '..OO.',
           '.....'],
          ['.....',
           '..O..',
           '.OO..',
           '.O...',
           '.....']]

Piece3 = [['..O..',
           '..O..',
           '..O..',
           '..O..',
           '.....'],
          ['.....',
           '.....',
           'OOOO.',
           '.....',
           '.....']]

Piece4 = [['.....',
           '.....',
           '.OO..',
           '.OO..',
           '.....']]

Piece5 = [['.....',
           '.O...',
           '.OOO.',
           '.....',
           '.....'],
          ['.....',
           '..OO.',
           '..O..',
           '..O..',
           '.....'],
          ['.....',
           '.....',
           '.OOO.',
           '...O.',
           '.....'],
          ['.....',
           '..O..',
           '..O..',
           '.OO..',
           '.....']]

Piece6 = [['.....',
           '...O.',
           '.OOO.',
           '.....',
           '.....'],
          ['.....',
           '..O..',
           '..O..',
           '..OO.',
           '.....'],
          ['.....',
           '.....',
           '.OOO.',
           '.O...',
           '.....'],
          ['.....',
           '.OO..',
           '..O..',
           '..O..',
           '.....']]

Piece7 = [['.....',
           '..O..',
           '.OOO.',
           '.....',
           '.....'],
          ['.....',
           '..O..',
           '..OO.',
           '..O..',
           '.....'],
          ['.....',
           '.....',
           '.OOO.',
           '..O..',
           '.....'],
          ['.....',
           '..O..',
           '.OO..',
           '..O..',
           '.....']]

PIECES = [Piece1,Piece2,Piece3,Piece4,Piece5,Piece6,Piece7]

#Tetris

