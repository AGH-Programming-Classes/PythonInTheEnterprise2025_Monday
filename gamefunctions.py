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
        try:
            # checking if user wants to exit
            row = str(input("Enter row (1-3) or press q to exit: "))
            if row == 'q':
                print("Thanks for playing!")
                exit()
            col = str(input("Enter column (1-3) or press q to exit: "))
            if col == 'q':
                print("Thanks for playing!")
                exit()
            #getting valid row
            row = int(input("Enter row (1-3) or press q to exit: ")) - 1
            while (row > 2 or row < 0):
                print("Invalid row number! Please enter a number between 1 and 3.")
                row = int(input("Enter row (1-3) or press q to exit: ")) - 1
            #getting valid column
            col = int(input("Enter column (1-3) or press q to exit: ")) - 1
            while (col > 2 or col < 0):
                print("Invalid column number! Please enter a number between 1 and 3.")
                col = int(input("Enter column (1-3) or press q to exit: ")) - 1

        #error if NaN
        except ValueError: 
            print("Invalid input! Please enter numbers only.")
            continue
        #checking if empty
        if board[row][col] == ' ':
            board[row][col] = mark
            move_done = True
        else:
            print("Invalid move! There's already a mark in the specified position!")