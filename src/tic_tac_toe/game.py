from tic_tac_toe.board import Board

class Gameplay:
    def __init__(self):
        self.board = Board()
    def boardStatus(self):
        count = 0
        for i in self.board.size:
            for j in self.board[i]:
                if self.board[i][j] != " ":
                    count += 1
        if count == 9:
            return "full"

    def winCheck(self):
        win = False
        for i in self.board.size:
        # check rows
            if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                if self.board[i][0] != " ":
                    win = True
        # check columns
            if self.board[0][i] == self.board[1][i] == self.board[2][i]:
                if self.board[0][i] != " ":
                    win = True
        # check diagonal
        if (self.board[0][0] == self.board[1][1] == self.board[2][2]) or (self.board[0][2] == self.board[1][1] == self.board[2][0]):
            if self.board[0][0] != " ":
                win = True
        return win

    def endgame(self):
        win = False
        draw = False

        if self.boardStatus(self.board) == "full":
            if self.winCheck(self.board) == False:
                draw = True
