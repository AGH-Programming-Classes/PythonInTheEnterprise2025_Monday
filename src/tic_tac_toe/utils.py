import enum
import typing
import random


def ask_for_name(player_tag) -> str:
    while True:
        name=input(f"Enter name of {player_tag}:")

        if name!="Bot":
            return name
import abc

class Printer(abc.ABC):
    @abc.abstractmethod
    def print(self, msg, **kwargs):
        pass
class NormalPrinter(Printer):
    def print(self, msg, **kwargs):
        print(msg, **kwargs)
class ColoringPrinter(Printer):
    def __init__(self, color_code):
        self.color_code = color_code
    def print(self, msg, **kwargs):
        kwargs_copy = dict(kwargs)
        kwargs_copy["end"] = ""
        print(f"\033[{30 + self.color_code}m", **kwargs_copy)
        print(msg, **kwargs_copy)
        print("\033[0m", **kwargs)
class UnderlinedReverseVideoDecoratingPrinter(Printer):
    def __init__(self, printer):
        self.printer = printer
    def print(self, msg, **kwargs):
        kwargs_copy = dict(kwargs)
        kwargs_copy["end"] = ""
        print(f"\033[4;7m", **kwargs_copy)
        self.printer.print(msg, **kwargs_copy)
        print("\033[0m", **kwargs)

printer = NormalPrinter()
def get_printer():
    return printer
def set_printer(new_printer):
    global printer
    printer = new_printer

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
                {self.board[0][0], self.board[0][1], self.board[0][2]},
                {self.board[1][0], self.board[1][1], self.board[1][2]},
                {self.board[2][0], self.board[2][1], self.board[2][2]},

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
            printer.print("X won")
        case GameState.PLAYER_2:
            printer.print("O won")
        case GameState.DRAW:
            printer.print("Draw")
        case GameState.UNFINISHED:
            printer.print("Unfinished")
    msg = "  A B C\n" + "\n".join(str(index+1) + " " + " ".join(row) for index,row in enumerate(state.board))
    printer.print(msg)
def ask_for_row():
    alphabet = ["1", "2", "3"]
    result = None
    while len(result := input("Specify row(1, 2 or 3): ")) != 1 or result not in alphabet:
        printer.print("Need one character (1, 2 or 3)")
    return ord(result) - 49
def ask_for_column():
    alphabet = ["A", "B", "C"]
    result = None
    while len(result := input("Specify column(A, B or C): ")) != 1 or result not in alphabet:
        printer.print("Need one character (A, B or C)")
    return ord(result) - 65
def ask_for_coordinates():
    row = ask_for_row()
    col = ask_for_column()
    return (row, col)

class PlayingStrategy(abc.ABC):
    @abc.abstractmethod
    def ask_for_move(self,State):
        pass

class HumanStrategy(PlayingStrategy):
    def ask_for_move(self,State):
        row = ask_for_row()
        col = ask_for_column()
        return (row, col)

class BotStrategy(PlayingStrategy):
    def ask_for_move(self, State):
        return (random.randint(0,2),random.randint(0,2))

class Play:
    def __init__(self,strategy: PlayingStrategy):
        self.strategy = strategy
    def play(self,state: State,p1_turn: bool):
        while True:
            coordinates = self.strategy.ask_for_move(state)
            if state.board[coordinates[0]][coordinates[1]]==" ":
                break

        while (invalid := not state.are_coordinates_valid(coordinates)) or\
                (tile := state.at_coordinates(coordinates)) != ' ':
            if invalid:
                printer.print("Invalid coordinates (out of board), asking again...")
            else:
                printer.print(f"Tile has been taken ('{tile}' sign has been placed)")
            coordinates = ask_for_coordinates()
        tile = "X" if p1_turn else "O"
        state.board[coordinates[0]][coordinates[1]] = tile
            

def ask_if_pvp():
    valid = ["p","b"]
    while True:
        result = input("Chcesz zagrać na bota(B), czy z innym graczem?(P) ")
        if result.lower() in valid:
            return result


