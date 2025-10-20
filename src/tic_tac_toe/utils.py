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
        diags = [
                {self.board[0][0], self.board[0][1], self.board[0][1]},
                {self.board[1][0], self.board[1][1], self.board[1][1]},
                {self.board[2][0], self.board[2][1], self.board[2][1]},

                {self.board[0][0], self.board[1][0], self.board[2][0]},
                {self.board[0][1], self.board[1][1], self.board[2][1]},
                {self.board[0][2], self.board[1][2], self.board[2][2]},

                {self.board[0][0], self.board[1][1], self.board[2][2]},
                {self.board[2][0], self.board[1][1], self.board[0][2]},
        ]
        non_draw = False
        for diag in diags:
            if " " in diag:
                non_draw = True
            if diag == {"X"}:
                return GameState.PLAYER_1
            if diag == {"O"}:
                return GameState.PLAYER_2
        return GameState.UNFINISHED if non_draw else GameState.DRAW
    def are_coordinates_valid(self, coordinates: typing.Tuple[int, int]):
        return 0 <= coordinates[0] < 3 and 0 <= coordinates[1] < 3
    def at_coordinates(self, coordinates: typing.Tuple[int, int]):
        return self.board[coordinates[0]][coordinates[1]]

def print_state(state: State):
    match state.state():
        case GameState.PLAYER_1:
            print("X won")
        case GameState.PLAYER_2:
            print("O won")
        case GameState.DRAW:
            print("Draw")
        case GameState.UNFINISHED:
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


