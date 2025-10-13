from src.tic_tac_toe.utils import GameState, ask_for_name, turn

def main():
    print("=== Tic Tac Toe ===")

    name1 = ask_for_name("player #1")
    name2 = ask_for_name("player #2")
    print(f"Starting game for {name1} and {name2}")

    state = None #todo: initialize state
    p1_turn = True
    while state.state() == GameState.UNFINISHED:
        turn(state, p1_turn)
        p1_turn = not p1_turn

if __name__ == "__main__":
    main()
