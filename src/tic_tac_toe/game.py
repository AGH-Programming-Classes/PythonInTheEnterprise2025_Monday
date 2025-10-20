from tic_tac_toe.board import Board

class Gameplay:
    def __init__(self):
        def boardStatus(Board):
            count = 0
            for i in board:
                for j in board[i]:
                    if board[i][j] != " ":
                        count += 1
            if count == 9:
                return "full"

        def winCheck(Board):
            for i in Board:
                if board[i][0] == board[i][1] == board[i][2]:
                    if board[i][0] != " ":
                        win = True

            # check rows
            # check columns
            # check diagonal

        def endgame(Board):
            win = False
            draw = False

            if boardStatus(Board) == "full":
                if winCheck(Board) == False:
                    draw = True
