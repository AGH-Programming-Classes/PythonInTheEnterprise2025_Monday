from tic_tac_toe.board import Board

class Utils:
    
    def boardStatus(board_state, board_size):
        count = 0
        for i in range(board_size):
            for j in range(board_size):
                if board_state[i][j] != " ":
                    count += 1
        if count == 9:
            return "full"


    def winCheck(board_state, board_size):
        win = False
        for i in range(board_size):
            # check rows
            if board_state[i][0] == board_state[i][1] == board_state[i][2]:
                if board_state[i][0] != " ":
                    win = True
            # check columns
            if board_state[0][i] == board_state[1][i] == board_state[2][i]:
                if board_state[0][i] != " ":
                    win = True
        # check diagonal
        if (board_state[0][0] == board_state[1][1] == board_state[2][2]) or (
                board_state[0][2] == board_state[1][1] == board_state[2][0]):
            if board_state[1][1] != " ":
                win = True
        return win


    def endgame(win, status):
        draw = False
        if status == "full":
            draw = True
        if win == True:
            return "WIN"
        if draw == True:
            return "DRAW"
        else:
            return "Continue"