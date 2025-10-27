from tic_tac_toe.board import Board
from GameUtils import Utils

class Gameplay:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]
        self.activeplayer = 0

    def nextPlayer(self):
        self.activeplayer = self.activeplayer ^ 1

    def CheckMove(self, move):
        board_state = self.board.getBoardState()
        i = (move - 1) // self.board.size
        j = (move - 1) % self.board.size
        if move == "":
            return False
        if move < 1 or move > 9:
            return False
        if board_state[i][j] != " ":
            return False
        else:
            return True

    def start(self):
        while True:
            self.board.draw()
            board_state = self.board.getBoardState()
            size = self.board.size
            symbol = self.players[self.activeplayer].getSymbol()
            move = self.players[self.activeplayer].makeMove(board_state)
            if self.CheckMove(move):
                self.board.setCell(move, symbol)
                end = Utils.endgame(board_state,size)
                if end == "Continue":
                    self.nextPlayer()
                else:
                    self.board.draw()
                    print("Game Over")
                    if end == "DRAW":
                        print("Draw")
                    if end == "WIN":
                        print(f"Winner is {symbol}")
                    break
            else:
                print("Invalid move, try again")



