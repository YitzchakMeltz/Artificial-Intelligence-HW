import pygame
import game
import math
from game import*
import winsound
import sys

ROWS=6
COLUMNS=7
SQUARESIZE = 80
WOFFSET = 10
HOFFSET = 50
PADDING = 7
RADIUS = int(SQUARESIZE/2 - 5)

BUTTON_WIDTH = 200
BUTTON_HEIGHT = 60

COMPUTER = 5 #Marks the computer's cells on the board
HUMAN = 1 #Marks the human's cells on the board
TIE=0 #The value of a tie

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)
GRAY = (220,220,220)

width = COLUMNS * SQUARESIZE  + WOFFSET*2
height = (ROWS + 1) * SQUARESIZE + HOFFSET + PADDING

def start_page():
    pygame.draw.rect(screen,GRAY,pygame.Rect(int(width/2)-(BUTTON_WIDTH/2), int(height/2)-(BUTTON_HEIGHT/2), BUTTON_WIDTH, BUTTON_HEIGHT))
    pygame.draw.rect(screen,GRAY,pygame.Rect(int(width/2)-(BUTTON_WIDTH/2), int(height/2)+BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT))
    start_msg()

def draw_board(board):
    for c in range(COLUMNS):
        for r in range(ROWS):
            pygame.draw.rect(screen, BLUE, (WOFFSET + c*SQUARESIZE, HOFFSET + r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, WHITE, (int(WOFFSET + c*SQUARESIZE+SQUARESIZE/2), int(HOFFSET + r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)

    if board:
        for c in range(COLUMNS):
            for r in range(ROWS):		
                if board[r][c] == COMPUTER:
                    pygame.draw.circle(screen, RED, (int(WOFFSET + c*SQUARESIZE+SQUARESIZE/2), int(HOFFSET + (r+1)*SQUARESIZE+SQUARESIZE/2)), RADIUS)
                elif board[r][c] == HUMAN: 
                    pygame.draw.circle(screen, YELLOW, (int(WOFFSET + c*SQUARESIZE+SQUARESIZE/2), int(HOFFSET + (r+1)*SQUARESIZE+SQUARESIZE/2)), RADIUS)

    pygame.display.update()

def button_click():

    clicked = -1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            return col

        if event.type == pygame.MOUSEBUTTONDOWN:
            posx = event.pos[0]
            posy = event.pos[1]

            if posx>191 and posx<389:
                if posy>279 and posy<337:
                    clicked = HUMAN
                    filename = 'C:/Users/hmeltz/Documents/GitHub/Artificial-Intelligence-HW/HW3/buttonPress.wav'
                    winsound.PlaySound(filename, winsound.SND_FILENAME)
                if posy>368 and posy<427:
                    clicked = COMPUTER
                    filename = 'C:/Users/hmeltz/Documents/GitHub/Artificial-Intelligence-HW/HW3/buttonPress.wav'
                    winsound.PlaySound(filename, winsound.SND_FILENAME)

    return clicked

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

def start_msg():
    myfont = pygame.font.SysFont("calibry", 75)
    label = myfont.render("Who Starts?", 1, BLACK)
    screen.blit(label, (140,110))

    myfont = pygame.font.SysFont("calibry", 30)
    label = myfont.render("USER", 1, BLACK)
    screen.blit(label, (262,int(height/2)-(BUTTON_HEIGHT/2)+22))

    myfont = pygame.font.SysFont("calibry", 30)
    label = myfont.render("COMPUTER", 1, BLACK)
    screen.blit(label, (230,int(height/2)+(BUTTON_HEIGHT/2)+52))

def print_gameover_msg(winner):
    myfont = pygame.font.SysFont("candara", 75)
    if winner == COMPUTER:
        label = myfont.render("   I Won!", 1, RED)
        screen.blit(label, (145,25))
        pygame.display.update()
        lose_sound()
    elif winner == HUMAN:
        label = myfont.render("    You Beat Me!", 1, RED)
        screen.blit(label, (10,25))
        pygame.display.update()
        won_sound()
    elif winner == TIE:
        label = myfont.render("It's a Tie!", 1, RED)
        screen.blit(label, (70,125))
    pygame.display.update()

def set_screen(ScreenType):
    if ScreenType == "Start Screen":
        screen.fill(WHITE)
        start_page()
    if ScreenType == "Game Screen":
        screen.fill(WHITE)
        draw_board(game.board)
    pygame.display.update()

def drop_sound():
    filename = 'C:/Users/hmeltz/Documents/GitHub/Artificial-Intelligence-HW/HW3/drop.wav'
    winsound.PlaySound(filename, winsound.SND_FILENAME)

def won_sound():
    filename = 'C:/Users/hmeltz/Documents/GitHub/Artificial-Intelligence-HW/HW3/wonSound.wav'
    winsound.PlaySound(filename, winsound.SND_FILENAME)

def lose_sound():
    filename = 'C:/Users/hmeltz/Documents/GitHub/Artificial-Intelligence-HW/HW3/loseSound.wav'
    winsound.PlaySound(filename, winsound.SND_FILENAME)

pygame.init()
 
size = (width, height)

pygame.display.set_caption(' Connect 4')
Icon = pygame.image.load("C:/Users/hmeltz/Documents/GitHub/Artificial-Intelligence-HW/HW3/Connect4Logo_1.0.0.png")
pygame.display.set_icon(Icon)

screen = pygame.display.set_mode(size)