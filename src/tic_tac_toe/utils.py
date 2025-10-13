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
    def state(self) -> GameState:
        # todo
        return GameState.UNFINISHED

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
    msg = "  a b c" + "\n".join(str(index+1) + " " + " ".join(row) for index,row in enumerate(state.board))
    print(msg
          )
def turn(state: State, p1_turn: bool):
    # todo
    pass
