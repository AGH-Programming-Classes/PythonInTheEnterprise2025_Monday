from gamefunctions import *

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

print_board(board)
while True:
    
    ## Player O's turn
    print("O's turn, make a move:")
    make_move(board, 'O')
    print_board(board)
    if winning_move(board, 'O'):
        print("O wins!")
        break
    ## Player X's turn
    print("X's turn, make a move:")
    make_move(board, 'X')
    print_board(board)
    if winning_move(board, 'X'):
        print("X wins!")
        break
    ## Check for draw (no more empty cells)
    if not any(' ' in row for row in board):
        print("It's a draw!")
        break

print("Thanks for playing!")