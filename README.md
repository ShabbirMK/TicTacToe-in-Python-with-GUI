# TicTacToe-in-Python-with-GUI

This is just a fun project with me exploring three things:
1. Building a GUI fully in Python: Using TKinter and PyGame
2. Exploring the MiniMax Algorithm
3. Falling in love with TicTacToe once again.

There are three full-fledged applications each implementing the same game however they are each implemented differently:
1. The CMD one using a CMD interface for playing the game between two players
2. The GUI is using the TKinter GUI interface for playing between two players
3. The Improved GUI is using PyGame, which is meant for designing the Games, for playering between two players as well as against the computer

The AI used in the computer makes the decision like:
1. First it checks if it possible to win for itself
2. Then it checks for preventing the win of the player
3. Then checks for the center box
4. If the PC is playing first, it will look for corners first and then edges to win
5. If the PC is playing second, it will look for edges first and then corners to draw when "X" has not occupied the center else it will look for corners first

The thought of the above logic on looking up for the patterns for the minimax algorithm which makes these decisions when playing against a person.
Try it out, let's see if you can win against the AI.
