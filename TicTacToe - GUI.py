from tkinter import *
import tkinter.messagebox

click = 1
tk = None


def game_start():
    '''
    The main function responsible for
    running the entire program
    '''
    global tk
    tk = Tk()
    tk.title("Tic Tac Toe - By Shabbir")

    def game_restart(player_num):
        global click
        '''
        To allow for game restarting with
        a simple yes-no question
        '''
        answer = tkinter.messagebox.askquestion(f'Player {player_num} wins!!!', 'Do you want to play again?')
        tk.destroy()
        click = 1
        if answer == 'yes':
            game_start()

    def win_condition(buttons):
        global click
        '''
        Checking for the win condition of
        each player
        '''
        if (button1["text"] == button2["text"] == button3["text"] == "X" or
            button4["text"] == button5["text"] == button6["text"] == "X" or
            button7["text"] == button8["text"] == button9["text"] == "X"):
            game_restart(1)

        elif (button1["text"] == button2["text"] == button3["text"] == "O" or
              button4["text"] == button5["text"] == button6["text"] == "O" or
              button7["text"] == button8["text"] == button9["text"] == "O"):
            game_restart(2)

        elif (button1["text"] == button4["text"] == button7["text"] == "X" or
              button2["text"] == button5["text"] == button8["text"] == "X" or
              button3["text"] == button6["text"] == button9["text"] == "X"):
            game_restart(1)

        elif (button1["text"] == button4["text"] == button7["text"] == "O" or
              button2["text"] == button5["text"] == button8["text"] == "O" or
              button3["text"] == button6["text"] == button9["text"] == "O"):
            game_restart(2)

        elif (button1["text"] == button5["text"] == button9["text"] == "X" or
              button3["text"] == button5["text"] == button7["text"] == "X"):
            game_restart(1)

        elif (button1["text"] == button5["text"] == button9["text"] == "O" or
              button3["text"] == button5["text"] == button7["text"] == "O"):
            game_restart(2)

        elif (button1["text"] != " " and button2["text"] != " " and
              button3["text"] != " " and button4["text"] != " " and
              button5["text"] != " " and button6["text"] != " " and
              button7["text"] != " " and button8["text"] != " " and
              button9["text"] != " "):
            answer = tkinter.messagebox.askquestion('It is a tie!!!', 'Do you want to play again?')
            tk.destroy()
            click = 1
            if answer == 'yes':
                game_start()

    def checker(buttons):
        '''
        It maintains the player 1
        and player 2 coordination
        '''
        global tk, click

        if click == 1 and buttons["text"] == " ":
            buttons["text"] = "X"
            click = 2

        elif click == 2 and buttons["text"] == " ":
            buttons["text"] = "O"
            click = 1

        win_condition(buttons)

    '''
    Button initialization
    '''
    button1 = Button(tk, text=" ", font="Times 26 bold", height=4, width=8, command=lambda: checker(button1))
    button1.grid(row=0, column=0, sticky=S + N + E + W)

    button2 = Button(tk, text=" ", font="Times 26 bold", height=4, width=8, command=lambda: checker(button2))
    button2.grid(row=0, column=1, sticky=S + N + E + W)

    button3 = Button(tk, text=" ", font="Times 26 bold", height=4, width=8, command=lambda: checker(button3))
    button3.grid(row=0, column=2, sticky=S + N + E + W)

    button4 = Button(tk, text=" ", font="Times 26 bold", height=4, width=8, command=lambda: checker(button4))
    button4.grid(row=1, column=0, sticky=S + N + E + W)

    button5 = Button(tk, text=" ", font="Times 26 bold", height=4, width=8, command=lambda: checker(button5))
    button5.grid(row=1, column=1, sticky=S + N + E + W)

    button6 = Button(tk, text=" ", font="Times 26 bold", height=4, width=8, command=lambda: checker(button6))
    button6.grid(row=1, column=2, sticky=S + N + E + W)

    button7 = Button(tk, text=" ", font="Times 26 bold", height=4, width=8, command=lambda: checker(button7))
    button7.grid(row=2, column=0, sticky=S + N + E + W)

    button8 = Button(tk, text=" ", font="Times 26 bold", height=4, width=8, command=lambda: checker(button8))
    button8.grid(row=2, column=1, sticky=S + N + E + W)

    button9 = Button(tk, text=" ", font="Times 26 bold", height=4, width=8, command=lambda: checker(button9))
    button9.grid(row=2, column=2, sticky=S + N + E + W)

    tk.mainloop()


game_start()


'''
lambda is used here because what follows command is a callback function.
In tkinter, the values are not passed into the callback since the callback
function is always called before the widget is made. Using lambda, this is
avoided as it allows for the value to be checked after widget creation
'''