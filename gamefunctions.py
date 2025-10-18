def winning_move(board, mark):
    # Checking rows, columns, and diagonals for a winning move
    for i in range(3):
        #checking rows
        if all([cell == mark for cell in board[i]]):
            return True
        #checking columns
        if all([board[j][i] == mark for j in range(3)]):
            return True
    #checking diagonals
    if all([board[i][i] == mark for i in range(3)]) or all([board[i][2 - i] == mark for i in range(3)]):
        return True
    return False

def print_board(board):
    i = 0
    for row in board:
        print(' | '.join(row))
        if(i < 2): print('-' * 10)
        i += 1

def make_move(board, mark):
    move_done = False
    while (move_done == False):
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))
        if board[row][col] == ' ':
            board[row][col] = mark
            move_done = True
        else:
            print("Invalid move! There's already a mark in the specified position!")
