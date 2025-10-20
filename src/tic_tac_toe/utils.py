import enum
import typing


def ask_for_name(player_tag) -> str:
    return input(f"Enter name of {player_tag}:")

class GameState(enum.Enum):
    PLAYER_1 = 1
    PLAYER_2 = 2
    DRAW = 3
    UNFINISHED = 4

class State:
    def __init__(self, board, p1_name, p2_name):
        self.board = board
        self.p1_name = p1_name
        self.p2_name = p2_name
    @staticmethod
    def new(p1_name, p2_name):
        return State([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]], p1_name, p2_name)
    def state(self) -> GameState:
        if self.check_if_win()=="X":
            return GameState.PLAYER_1
        if self.check_if_win()=="O":
            return GameState.PLAYER_2
        if self.check_if_draw:
            return GameState.DRAW
        return GameState.UNFINISHED
    def are_coordinates_valid(self, coordinates: typing.Tuple[int, int]):
        return 0 <= coordinates[0] < 3 and 0 <= coordinates[1] < 3
    def at_coordinates(self, coordinates: typing.Tuple[int, int]):
        return self.board[coordinates[0]][coordinates[1]]
    def check_if_draw(self):
        for row in self.board:
            for p in row:
                if p==" ":
                    return False
        return True
    def check_if_win(self):
        if any(len(set(row)) == 1 and row[0]=="X" for row in self.board):
            return "X"
        if any(len(set(row)) == 1 and row[0]=="O" for row in self.board):
            return "O"
        
        if len(set([self.board[i][i]] for i in range(3))) == 1 and self.board[0][0]=="X":
            return "X"
        
        if len(set([self.board[i][i]] for i in range(3))) == 1 and self.board[0][0]=="O":
            return "O"

        if len(set([self.board[i][2 - i]] for i in range(3))) == 1 and self.board[0][2]=="X":
            return "X"
        
        if len(set([self.board[i][2 - i]] for i in range(3))) == 1 and self.board[0][2]=="O":
            return "O"
        
        for col in range(3):
            if self.board[0][col]==self.board[1][col]==self.board[2][col]:
                if self.board[0][col]=="X":
                    return "X"
                else:
                    return "O"

        return False    

def print_state(state: State):
    match state.state():
        case 1:
            print("X won")
        case 2:
            print("O won")
        case 3:
            print("Draw")
        case 4:
            print("Unfinished")
    msg = "  a b c\n" + "\n".join(str(index+1) + " " + " ".join(row) for index,row in enumerate(state.board))
    print(msg)
def ask_for_row():
    alphabet = ["1", "2", "3"]
    result = None
    while len(result := input("Specify row(1, 2 or 3): ")) != 1 or result not in alphabet:
        print("Need one character (1, 2 or 3)")
    return ord(result) - 49
def ask_for_column():
    alphabet = ["A", "B", "C"]
    result = None
    while len(result := input("Specify column(A, B or C): ")) != 1 or result not in alphabet:
        print("Need one character (A, B or C)")
    return ord(result) - 65
def ask_for_coordinates():
    row = ask_for_row()
    col = ask_for_column()
    return (row, col)
def turn(state: State, p1_turn: bool):
    coordinates = ask_for_coordinates()
    while (invalid := not state.are_coordinates_valid(coordinates)) or\
            (tile := state.at_coordinates(coordinates)) != ' ':
        if invalid:
            print("Invalid coordinates (out of board), asking again...")
        else:
            print(f"Tile has been taken ('{tile}' sign has been placed)")
        coordinates = ask_for_coordinates()
    tile = "X" if p1_turn else "O"
    state.board[coordinates[0]][coordinates[1]] = tile


