import enum
import typing


def ask_for_name(player_tag) -> str:
    return input(f"Enter name of {player_tag}:")

class GameState(enum.EnumType):
    PLAYER_1 = 1
    PLAYER_2 = 2
    DRAW = 3
    UNFINISHED = 4

class State:
    def __init__(self, board, p1_name, p2_name):
        self.board = board
        self.p1_name = p1_name
        self.p2_name = p2_name
    def state(self) -> GameState:
        # todo
        return GameState.UNFINISHED

def print_state(state: State):
    # todo
    pass
def turn(state: State, p1_turn: bool):
    # todo
    pass
