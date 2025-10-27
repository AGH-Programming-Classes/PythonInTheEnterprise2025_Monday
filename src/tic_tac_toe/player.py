import random

class Player:
    def __init__(self, symbol, strategy):
        self.symbol = symbol
        self.strategy = strategy

    def getSymbol(self):
        return self.symbol
    
    def makeMove(self, board_state): 
        print(f"Player {self.symbol} moves!")
        return self.strategy.makeMove(self.symbol, board_state)

class PlayerStrategy:
    def makeMove(self, symbol, board_state): raise NotImplementedError

    def getValid(self, board_state):
        valid = []
        size = len(board_state)
        for i in range(size):
            for j in range(size):
                if board_state[i][j] == ' ':
                    valid.append(i * size + j + 1) 
        return valid

class Manual(PlayerStrategy):
    def makeMove(self, symbol, board_state):
        return int(input("Enter field number: "))
    
class Random(PlayerStrategy):
    def makeMove(self, symbol, board_state):
        return random.choice(self.getValid(board_state))