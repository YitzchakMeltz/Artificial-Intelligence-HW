import pygame
import game
import math
from game import*

ROWS=6
COLUMNS=7
SQUARESIZE = 80
RADIUS = int(SQUARESIZE/2 - 5)

COMPUTER = 5 #Marks the computer's cells on the board
HUMAN = 1 #Marks the human's cells on the board
TIE=0 #The value of a tie

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

def draw_board(board):
    for c in range(COLUMNS):
        for r in range(ROWS):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)

    if board:
        for c in range(COLUMNS):
            for r in range(ROWS):		
                if board[r][c] == COMPUTER:
                    pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), int((r+1)*SQUARESIZE+SQUARESIZE/2)), RADIUS)
                elif board[r][c] == HUMAN: 
                    pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), int((r+1)*SQUARESIZE+SQUARESIZE/2)), RADIUS)

    pygame.display.update()

def handle_events():

    col = -1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            return col

        if event.type == pygame.MOUSEBUTTONDOWN:
            posx = event.pos[0]
            col = int(math.floor(posx/SQUARESIZE))

    return col

def sleep_screen(sec):
    pygame.time.wait(sec*1000)

def print_gameover_msg(winner):
    myfont = pygame.font.SysFont("monospace", 75)
    if winner == COMPUTER:
        label = myfont.render("I Won!", 1, RED)
        screen.blit(label, (145,5))
    elif winner == HUMAN:
        label = myfont.render("You Beat Me!", 1, RED)
        screen.blit(label, (20,5))
    elif winner == TIE:
        label = myfont.render("It's a Tie!", 1, RED)
        screen.blit(label, (70,5))
    pygame.display.update()

pygame.init()

width = COLUMNS * SQUARESIZE
height = (ROWS + 1) * SQUARESIZE
 
size = (width, height)

pygame.display.set_caption(' Connect 4')
Icon = pygame.image.load("C:/Users/hmeltz/Documents/GitHub/Artificial-Intelligence-HW/HW3/Connect4Logo_1.0.0.png")
pygame.display.set_icon(Icon)

screen = pygame.display.set_mode(size)
draw_board(game.board)
pygame.display.update()