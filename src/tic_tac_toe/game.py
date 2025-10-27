from tic_tac_toe.board import Board

class Gameplay:
    def __init__(self):
        self.board = Board()
        self.activeplayer = "X"

    def boardStatus(self):
        board_state = self.board.getBoardState()
        count = 0
        for i in range(self.board.size):
            for j in range(self.board.size):
                if board_state[i][j] != " ":
                    count += 1
        if count == 9:
            return "full"

    def winCheck(self):
        win = False
        board_state = self.board.getBoardState()
        for i in range(self.board.size):
        # check rows
            if board_state[i][0] == board_state[i][1] == board_state[i][2]:
                if board_state[i][0] != " ":
                    win = True
        # check columns
            if board_state[0][i] == board_state[1][i] == board_state[2][i]:
                if board_state[0][i] != " ":
                    win = True
        # check diagonal
        if (board_state[0][0] == board_state[1][1] == board_state[2][2]) or (board_state[0][2] == board_state[1][1] == board_state[2][0]):
            if board_state[1][1] != " ":
                win = True
        return win

    def endgame(self):
        draw = False
        win = self.winCheck()

        if self.boardStatus() == "full":
            draw = True

        if win == True:
            return "WIN"
        if draw == True:
            return "DRAW"
        else:
            return "Continue"

    def start(self):
        while True:
            self.board.draw()
            p=int(input(f"Player {self.activeplayer} enters: "))
            # chech if move legal
            self.board.setCell(p, self.activeplayer)
            end = self.endgame()
            if end == "Continue":
                self.activeplayer = "O" if self.activeplayer == "X" else "X"
            else:
                self.board.draw()
                print("Game Over")
                if end == "DRAW":
                    print("Draw")
                if end == "WIN":
                    print(f"Winner is {self.activeplayer}")
                break



