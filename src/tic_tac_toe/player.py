class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def getSymbol(self):
        return self.symbol
    
    def makeMove(self):
        return int(input("Podaj numer:"))