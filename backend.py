from gamefunctions import *
import os


board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

logger("New turn started")
print_board(board)
while True:
    
    ## Player O's turn
    print("O's turn, make a move:")
    make_move(board, 'O')
    os.system('cls' if os.name == 'nt' else 'clear')
    print_board(board)
    if winning_move(board, 'O'):
        print("O wins!")
        logger("O has won the game")
        break
    ## Player X's turn
    if not any(' ' in row for row in board):
        print("It's a draw!")
        logger("The game ended in a draw")
        break
    print("X's turn, make a move:")
    make_move(board, 'X')
    os.system('cls' if os.name == 'nt' else 'clear')
    print_board(board)
    if winning_move(board, 'X'):
        print("X wins!")
        logger("X has won the game")
        break
    ## Check for draw (no more empty cells)


print("Thanks for playing!")

## version with class

class Game:
    def __init__(self):
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]

    def play(self):
        print_board(self.board)
        self.notify("start", {"message": "New game started"})
        
        