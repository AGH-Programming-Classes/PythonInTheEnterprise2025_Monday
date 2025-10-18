from gamefunctions import *

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

while True:
    print_board(board)
    ## Player O's turn
    make_move(board, 'O')
    if winning_move(board, 'O'):
        print("O wins!")
        break
    ## Player X's turn
    make_move(board, 'X')
    if winning_move(board, 'X'):
        print("X wins!")
        break
    ## Check for draw (no more empty cells)
    if not any(' ' in row for row in board):
        print("It's a draw!")
        break
print_board(board)
print("Thanks for playing!")