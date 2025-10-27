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
    print( " 1   2   3")
    for row in board:

        print(str(i+1) + " " + ' | '.join(row))
        if(i < 2): print( " " + '-' * 10)
        i += 1

def make_move(board, mark):
    move_done = False
    while (move_done == False):
        try:
            # checking if user wants to exit
            row_input = input("Enter row (1-3) or press q to exit: ").strip()
            if row_input .lower()== 'q':
                print("Thanks for playing!")
                exit()
            row = int(row_input) - 1
            if row not in range(3):
                print("Invalid row number! Please enter a number between 1 and 3.")
                continue
                
            col_input = input("Enter column (1-3) or press q to exit: ").strip()
            if col_input.lower() == 'q':
                print("Thanks for playing!")
                exit()
            col = int(col_input) - 1
            if row not in range(3):
                print("Invalid row number! Please enter a number between 1 and 3.")
                continue
            
        #error if NaN
        except ValueError: 
            print("Invalid input! Please enter numbers only.")
            continue
        #checking if empty
        if board[row][col] == ' ':
            board[row][col] = mark
            move_done = True
            logger(f"Player {mark} placed his mark on row {row + 1}, column {col + 1}")
        else:
            print("Invalid move! There's already a mark in the specified position!")

def logger(message):
    with open("game_log.txt", "a") as log_file:
        log_file.write(message + "\n")