from src.tic_tac_toe.utils import GameState, State, ask_for_name, print_state, turn

def main():
    print("=== Tic Tac Toe ===")

    name1 = ask_for_name("player #1")
    name2 = ask_for_name("player #2")
    print(f"Starting game for {name1} and {name2}")

    state = State.new(name1, name2)
    p1_turn = True
    while state.state() == GameState.UNFINISHED:
        print_state(state)
        turn(state, p1_turn)
        p1_turn = not p1_turn

    print_state(state)

if __name__ == "__main__":
    main()
