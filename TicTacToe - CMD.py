'''
To create a cmd window size which is more immersive
'''
import os
os.system("mode con cols=50 lines=21")


class tictactoc():

    def __init__(self):
        self.game_list = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.rounds = -1
        self.is_ready = False
        self.win = False
        self.draw = False
        self.is_game_over = False

    def display(self):
        '''
        Will display the arrangement and
        will mark the start of the next
        round
        '''
        print("\n")
        print(f"\t\t {self.game_list[1]} | {self.game_list[2]} | {self.game_list[3]}")
        print("\t\t-----------")
        print(f"\t\t {self.game_list[4]} | {self.game_list[5]} | {self.game_list[6]}")
        print("\t\t-----------")
        print(f"\t\t {self.game_list[7]} | {self.game_list[8]} | {self.game_list[9]}")
        print("\n")
        self.rounds += 1

    def add_piece(self, p, pos):
        '''
        Takes the position, the symbol and
        Modifies the list
        '''
        self.game_list[pos] = p

    def check_win(self, p):
        '''
        Checks for the win condition for
        the given symbol
        '''
        for index in range(1, 4):
            if self.game_list[index] == self.game_list[index + 3] == self.game_list[index + 6] == p:
                self.win = True
                self.is_game_over = True

        if not self.win:
            for index in range(1, 10, 3):
                if self.game_list[index] == self.game_list[index + 1] == self.game_list[index + 2] == p:
                    self.win = True
                    self.is_game_over = True

        if self.game_list[1] == self.game_list[5] == self.game_list[9] == p:
            self.win = True
            self.is_game_over = True

        elif self.game_list[3] == self.game_list[5] == self.game_list[7] == p:
            self.win = True
            self.is_game_over = True

    def check_draw(self):
        '''
        Checks for the draw condition
        '''
        if self.rounds == 9 and not self.win:
            self.draw = True
            self.is_game_over = True


def inputhandle():
    is_ready = "n"
    while True:
        p1 = input("Player 1, enter your choice of symbol - X or O: ").upper()
        while not (p1 == "X" or p1 == "O"):
            p1 = input("Enter a valid symbol! X or O: ").upper()

        is_ready = input("Are you ready? Enter Yes or No: ").lower()
        while not (is_ready in ["yes", "no", "y", "n"]):
            is_ready = input("Please enter Yes or No. Are you ready?: ").lower()

        if is_ready in ["y", "yes"]:
            game.is_ready = True
            break

    print("\n")
    del is_ready

    if p1 == "X":
        print("\t  Player 1 will start the game")
        first = 1
        second = 2
    else:
        print("\t  Player 2 will start the game")
        first = 2
        second = 1
    del p1
    return first, second


print("Welcome to Tic Tac Toe - By Shabbir\n")
game = tictactoc()
first, second = inputhandle()
while game.is_ready:
    game.display()

    while not(game.is_game_over):
        while True:
            try:
                pos = int(input(f"\n    Player {first}, enter your desired position: "))
                if not 1 <= pos <= 9:
                    print("\nEnter a valid position!")
                elif game.game_list[pos] != " ":
                    print("\nEntered position is already filled")
                else:
                    break
            except ValueError:
                print("\nEnter a valid number as position")

        game.add_piece("X", pos)

        game.display()
        game.check_win("X")
        game.check_draw()

        if game.win:
            print(f"Congratulations Player {first}, you have won!!!\n")
        elif game.draw:
            print("There is a tie!!!\n")

        else:

            while True:
                try:
                    pos = int(input(f"\n    Player {second}, enter your desired position: "))
                    if not 1 <= pos <= 9:
                        print("\nEnter a valid position!")
                    elif game.game_list[pos] != " ":
                        print("\nEntered position is already filled")
                    else:
                        break
                except ValueError:
                    print("\nEnter a valid number as position")

            game.add_piece("O", pos)

            game.display()
            game.check_win("O")

            if game.win:
                print(f"Congratualations Player {second}, you have won!!!\n")

    if game.is_game_over:
        play_game = input("Would you like to play again? Enter Yes or No: ").lower()
        while not (play_game in ["yes", "no", "y", "n"]):
            play_game = input("Please enter either Yes or No! : ")
        if play_game == "yes" or play_game == "y":
            print("\n" * 100)
            game = tictactoc()
            first, second = inputhandle()
        else:
            game.is_ready = False


print("\nThank you for playing Tic Tac Toe - By Shabbir")
