import random

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

class Observer:
    def update(self, message):
        raise NotImplementedError

class Subject:
    def __init__(self):
        self.observers = []

    def add (self, observer):
        self.observers.append(observer)

    def remove(self, observer):
        self.observers.remove(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

class Logger(Observer):
    def update(self, message):
        with open("game_log.txt", "a") as log_file:
            log_file.write(message + "\n")

class Console(Observer):
    def update(self, message):
        print(message)

# base strategy interface
class MoveStrategy:
    def make_move(self, game, mark):
        raise NotImplementedError("Each strategy must implement make_move(game, mark) method.")
    
    
# asks user for input, game for two players
class HumanMoveStrategy(MoveStrategy):
    def make_move(self, game, mark):
        game.make_move(mark)

# one player - with computer, which picks empty cell randomly
class ComputerMoveStrategy(MoveStrategy):
    def make_move(self, game, mark):
        # find empty cells
        empty_cells = [(r, c) for r in range(3) for c in range(3) if game.board[r][c] == ' ']
        if empty_cells:
            row, col = random.choice(empty_cells)
            game.board[row][col] = mark
            game.notify(f"Computer placed '{mark}' on row {row+1}, column {col+1}")
class Player:
    def __init__(self, mark, strategy: MoveStrategy):
        self.mark = mark
        self.strategy = strategy

    def play(self, game):
        self.strategy.make_move(game, self.mark)