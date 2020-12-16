# importing the required libraries
import pygame as pg
import os
import time
from pygame.locals import *
import copy
import random

# Declaring the global variables
# Current player symbol
symbol = 'X'

# Storing the winner's value at an instance
winner = None

# To check for a draw
draw = None

# Setting the dimensions of the board
width = 500
height = 500

# Setting the design of the board
# Game window background colour
white = (255, 255, 255)
# Game board cells boundary colour
line_color = (0, 0, 0)
# Layout of the 3 * 3 board
board = [[None] * 3, [None] * 3, [None] * 3]

# initializing the pygame window
pg.init()

# setting fps manually
fps = 30

# this is used to track time
CLOCK = pg.time.Clock()


# Setting up the GUI
screen = pg.display.set_mode((width, height + 100), 0, 32)

# Providing a name to the window
pg.display.set_caption("Tic Tac Toe")

# Setting the cover and cell images
initiating_window = pg.image.load(os.path.join(
    os.path.join(os.getcwd(), "media"), "Cover.jpeg"))
x_img = pg.image.load(os.path.join(
    os.path.join(os.getcwd(), "media"), "X.png"))
y_img = pg.image.load(os.path.join(
    os.path.join(os.getcwd(), "media"), "O.png"))

# Padding for the images in each cell
padding = (width // 3 - width // 4) // 2
# Resizing images
initiating_window = pg.transform.scale(initiating_window, (width, height))
x_img = pg.transform.scale(x_img, (width // 4, height // 4))
o_img = pg.transform.scale(y_img, (width // 4, height // 4))


class Button():
    def __init__(self, color, x, y, width, height, text, border_width, border_radius):
        self.color = color
        self.rect = Rect(x + 2, y + 2, width - 8, height - 4)
        self.text = text
        self.border_width = border_width
        self.border_radius = border_radius

    def drawButton(self):
        '''
        We are rendering the button as per the initialization
        '''
        pg.draw.rect(surface=screen,
                     color=self.color,
                     rect=self.rect,
                     width=self.border_width,
                     border_radius=self.border_radius
                     )

        font = pg.font.Font(None, 30)
        text = font.render(self.text, 1, (255, 255, 255))
        screen.blit(text,
                    (self.rect[0] + (self.rect[2] - text.get_width()) // 2,
                     self.rect[1] + (self.rect[3] - text.get_height()) // 2))

        pg.display.update()


def createFirstWindow():
    '''
    This is to create the first page of the game showing the buttons
    for playing against PC or person
    '''
    # Displaying over the screen
    screen.blit(source=initiating_window, dest=(0, 0))

    screen.fill(color=(0, 0, 0), rect=Rect(0, height, width, 100))
    OneVsOneButton = Button(color=(255, 0, 0),
                            x=0,
                            y=height,
                            width=width // 2,
                            height=100,
                            text="Play against Person",
                            border_width=5,
                            border_radius=10
                            )
    OneVsOneButton.drawButton()

    font = pg.font.Font(None, 30)
    text = font.render("Play against PC", 1, (255, 255, 255))
    screen.blit(text,
                (width // 2 + (width // 2 - text.get_width()) // 2,
                 height + (50 - text.get_height()) // 2))

    PlayAgainstPCButtonAsX = Button(color=(255, 0, 0),
                                    x=width // 2,
                                    y=height + 50,
                                    width=width // 4,
                                    height=50,
                                    text="Play as X",
                                    border_width=1,
                                    border_radius=10
                                    )
    PlayAgainstPCButtonAsO = Button(color=(255, 0, 0),
                                    x=width // 2 + width // 4,
                                    y=height + 50,
                                    width=width // 4,
                                    height=50,
                                    text="Play as O",
                                    border_width=1,
                                    border_radius=10
                                    )

    encasingButton = Button(color=(255, 0, 0),
                            x=width // 2,
                            y=height,
                            width=width // 2,
                            height=100,
                            text="",
                            border_width=5,
                            border_radius=10
                            )

    SimulateButton = Button(color=(0, 0, 0),
                            x=width // 2 + width // 4,
                            y=5,
                            width=width // 4,
                            height=35,
                            text="Simulate",
                            border_width=0,
                            border_radius=0
                            )

    PlayAgainstPCButtonAsX.drawButton()
    PlayAgainstPCButtonAsO.drawButton()
    encasingButton.drawButton()
    SimulateButton.drawButton()
    # Updating the display
    pg.display.update()


def createSecondWWindow():
    '''
    This is to set up the board in terms of the borders as per
    the design set up in the global variables
    '''
    screen.fill(white)

    # Drawing vertical lines
    pg.draw.line(surface=screen,
                 color=line_color,
                 start_pos=(width / 3, 0),
                 end_pos=(width / 3, height),
                 width=7)

    pg.draw.line(surface=screen,
                 color=line_color,
                 start_pos=(width / 3 * 2, 0),
                 end_pos=(width / 3 * 2, height),
                 width=7)

    # Drawing horizontal lines
    pg.draw.line(surface=screen,
                 color=line_color,
                 start_pos=(0, height / 3),
                 end_pos=(width, height / 3),
                 width=7)

    pg.draw.line(surface=screen,
                 color=line_color,
                 start_pos=(0, height / 3 * 2),
                 end_pos=(width, height / 3 * 2),
                 width=7)

    pg.display.update()


def showStatus():
    '''
    The function is responsible for handling the current game situation
    i.e. If the game has ended then who is the winner or has it drawn or
    whose chance is it to play right now if the game has not ended
    '''
    global winner, draw

    if winner is None:
        message = symbol.upper() + "'s Turn"
    else:
        message = winner.upper() + " won !"
    if draw:
        message = "Game Draw !"

    # Selecting the font for the above text
    # We can use custom font here
    font = pg.font.Font(None, 30)

    # Setting the properties to the text
    # [text, antialias, color]
    text = font.render(message, 1, (255, 255, 255))

    # copy the rendered message onto the board
    # creating a small block at the bottom of the main display
    # rect - > (left, top, width, height)
    screen.fill(color=(0, 0, 0), rect=Rect(0, height, width, 100))
    text_rect = text.get_rect(center=(width / 2, height + 50))
    screen.blit(text, text_rect)
    pg.display.update()


def drawSymbol(row, col):
    '''
    Here we are drawing the "X" or "O" as per the mouse_click.
    The board is updated and the image is printed on the screen
    '''
    global symbol, board, padding

    # Adding the padding the image and getting the correct
    # co-ordinates for the image to be placed
    posx = (width / 3) * (row - 1) + padding
    posy = (height / 3) * (col - 1) + padding

    board[row - 1][col - 1] = symbol

    # Pasting the corresponding symbol on the cell
    # Changing the symbol as well
    if(symbol == 'X'):
        screen.blit(x_img, (posy, posx))
        symbol = 'O'

    else:
        screen.blit(o_img, (posy, posx))
        symbol = 'X'
    pg.display.update()


def checkWinConditionPlayingPC(board):
    '''
    Just a copy of the other similar function which just checks for the condition
    but doesn't update the board
    '''
    for index, row in enumerate(board):
        if (row[0] == row[1] == row[2]) and row[0]:
            return True

    for col in range(0, 3):
        if (board[0][col] == board[1][col] == board[2][col]) and board[0][col]:
            return True

    if (board[0][0] == board[1][1] == board[2][2]) and board[0][0]:
        return True

    if (board[0][2] == board[1][1] == board[2][0]) and board[0][2]:
        return True

    return False


def checkWinCondition():
    '''
    We check for win condition if three symbols align
    along the column or the row or the diagonal
    '''
    global board, winner, draw

    # Checking for win condition in a row
    # Either they are all "X"s or "O"s but not None
    for index, row in enumerate(board):
        if (row[0] == row[1] == row[2]) and row[0]:
            winner = row[0]
            pg.draw.line(
                surface=screen,
                color=(250, 0, 0),
                start_pos=(width / 6, (index + 1) * height / 3 - height / 6),
                end_pos=(5 * width / 6, (index + 1) * height / 3 - height / 6),
                width=4)

            break

    # Checking for win condition in a column
    # Either they are all "X"s or "O"s but not None
    for col in range(0, 3):
        if (board[0][col] == board[1][col] == board[2][col]) and board[0][col]:
            winner = board[0][col]
            pg.draw.line(
                surface=screen,
                color=(250, 0, 0),
                start_pos=((col + 1) * width / 3 - width / 6, height / 6),
                end_pos=((col + 1) * width / 3 - width / 6, 5 * height / 6),
                width=4)

            break

    # Check for win condition along the diagonal
    # Either they are all "X"s or "O"s and not None
    if (board[0][0] == board[1][1] == board[2][2]) and board[0][0]:
        # L to R
        winner = board[0][0]
        pg.draw.line(
            surface=screen,
            color=(250, 0, 0),
            start_pos=(width / 6, height / 6),
            end_pos=(5 * width / 6, 5 * width / 6),
            width=4)

    if (board[0][2] == board[1][1] == board[2][0]) and board[0][2]:
        # R to L
        winner = board[0][2]
        pg.draw.line(
            surface=screen,
            color=(250, 0, 0),
            start_pos=(5 * width / 6, height / 6),
            end_pos=(width / 6, 5 * height / 6),
            width=4)

    if(all([all(row) for row in board]) and winner == None):
        draw = True
    showStatus()


def userClick():
    '''
    This will be the main function to decide what exactly
    to do for a given mouse click on the board
    '''
    # Get coordinates of mouse click
    x, y = pg.mouse.get_pos()

    # Get row and column of mouse click
    col = int(x / width * 3) + 1
    row = int(y / height * 3) + 1

    if row > 3 or col > 3:
        return

    # Using these co-ordinates, we can check if the
    # the cell is empty or not and decide. The cell
    # will be filled and win condition would be checked

    if(board[row - 1][col - 1] == None):
        drawSymbol(row, col)
        checkWinCondition()


def reset_game(current_symbol='X'):
    '''
    Here we aim to reset the board in order to play again
    '''
    global board, winner, symbol, draw
    symbol = current_symbol
    draw = False
    winner = None
    board = [[None] * 3, [None] * 3, [None] * 3]


def movebyPC():
    '''
    Here we are testing for the best move that the PC
    should use against the player to not make him win
    '''
    # Check if a win condition is being achieved or not
    players = []
    players.append(symbol)
    players.append("X") if "O" == symbol else players.append("O")
    for player in players:
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] is None:
                    tmp = copy.deepcopy(board)
                    tmp[i][j] = player
                    if checkWinConditionPlayingPC(tmp):
                        drawSymbol(i + 1, j + 1)
                        checkWinCondition()
                        return

    # In case a win condition cannot be reached, the PC
    # would try to place the symbol first in the center
    # or it will try to place it in the corners and finally
    # in the order remaining spots

    if board[1][1] is None:
        drawSymbol(2, 2)
        return

    if symbol == "X" or (board[1][1] == "X" and symbol == "O"):
        # In order to win the computer will search for corners first
        # and then look for edges
        corner = [(0, 0), (2, 0), (0, 2), (2, 2)]
        corner = [(x, y) for x, y in corner if board[x][y] is None]
        if len(corner) > 0:
            corner = random.choice(corner)
            drawSymbol(corner[0] + 1, corner[1] + 1)
            return

        edges = [(1, 0), (2, 1), (0, 1), (1, 2)]
        edges = [(x, y) for x, y in edges if board[x][y] is None]
        if len(edges) > 0:
            edges = random.choice(edges)
            drawSymbol(edges[0] + 1, edges[1] + 1)
            return
    else:
        # In order to draw the match now against the player, the computer
        # will search for edges first and then for corners
        edges = [(1, 0), (2, 1), (0, 1), (1, 2)]
        edges = [(x, y) for x, y in edges if board[x][y] is None]
        if len(edges) > 0:
            edges = random.choice(edges)
            drawSymbol(edges[0] + 1, edges[1] + 1)
            return

        corner = [(0, 0), (2, 0), (0, 2), (2, 2)]
        corner = [(x, y) for x, y in corner if board[x][y] is None]
        if len(corner) > 0:
            corner = random.choice(corner)
            drawSymbol(corner[0] + 1, corner[1] + 1)
            return


def OneVsOne():
    '''
    This is the main driver function to for playing
    against a person.
    '''
    createSecondWWindow()
    showStatus()

    while True:
        for event in pg.event.get():
            if event.type == MOUSEBUTTONDOWN:
                userClick()
                if (winner or draw):
                    reset_game()
                    time.sleep(5)
                    main()

        pg.display.update()
        CLOCK.tick(fps)


def AgainstPC(PCfirst):
    '''
    This is the main driver function for playing against PC
    '''
    createSecondWWindow()
    showStatus()
    if PCfirst:
        # The computer plays first
        movebyPC()

    while True:
        for event in pg.event.get():
            if event.type == MOUSEBUTTONDOWN:
                userClick()
                checkWinCondition()
                if (winner or draw):
                    reset_game()
                    time.sleep(5)
                    main()
                movebyPC()
                checkWinCondition()
                if (winner or draw):
                    reset_game()
                    time.sleep(5)
                    main()

        pg.display.update()
        CLOCK.tick(fps)


def simulator():
    '''
    This is just an AI v/s AI game which will always lead to
    a draw.
    '''
    createSecondWWindow()
    showStatus()
    while True:
        for event in pg.event.get():
            time.sleep(2)
            movebyPC()
            checkWinCondition()
            if (winner or draw):
                time.sleep(2)
                reset_game()
                main()
            time.sleep(2)
            movebyPC()
            checkWinCondition()
            if (winner or draw):
                time.sleep(2)
                reset_game()
                main()


def main():
    createFirstWindow()
    # First we will choose if we want to play against PC
    # or against a person
    while True:
        for event in pg.event.get():
            if event.type == MOUSEBUTTONDOWN:
                x, y = pg.mouse.get_pos()
                if y > 5 and y < 40 and x > width // 2 + width // 4:
                    simulator()
                y = y - height - 50
                if y > 0 and x < width // 2:
                    OneVsOne()
                elif y > 0 and x > width // 2:
                    if x < 3 * width // 4:
                        AgainstPC(PCfirst=False)
                    else:
                        AgainstPC(PCfirst=True)

            elif event.type == QUIT:
                pg.quit()
                exit()


if __name__ == '__main__':
    main()
