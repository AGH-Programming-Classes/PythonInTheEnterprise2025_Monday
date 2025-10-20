from src.tic_tac_toe.utils import ColoringPrinter, GameState, NormalPrinter, State,\
  UnderlinedReverseVideoDecoratingPrinter, ask_for_name, get_printer, print_state, set_printer, turn, ask_if_pvp


def ask_boolean(question):
    inpt = input(f"{question}" + " (true, t, yes or y for yes): ")
    return inpt.lower() in {"true", "t", "yes", "y"}

def ask_for_reverse_video_and_underlining():
    return ask_boolean("Do you want reverse video (swap fg and bg colors) and underline on all output?")
def ask_for_color():
    color = input("Name color you want for output (0 - 7), if other input, default will be assumed: ")
    if color not in "01234567":
        return None
    return int(color)

def main():
    print("=== Tic Tac Toe ===")
    if ask_if_pvp()=="P":
        name1 = ask_for_name("player #1")
        name2 = ask_for_name("player #2")
    else:
        name1 = ask_for_name("player #1")
        name2 = "Bot"
    print(f"Starting game for {name1} and {name2}")
    color = ask_for_color()
    if color != None:
        set_printer(ColoringPrinter(color))
    rev_video = ask_for_reverse_video_and_underlining()
    if rev_video:
        set_printer(UnderlinedReverseVideoDecoratingPrinter(get_printer()))

    name1 = ask_for_name("player #1")
    name2 = ask_for_name("player #2")
    get_printer().print(f"Starting game for {name1} and {name2}")

    state = State.new(name1, name2)
    p1_turn = True
    while state.state() == GameState.UNFINISHED:
        print_state(state)
        turn(state, p1_turn)
        p1_turn = not p1_turn

    print_state(state)


if __name__ == "__main__":
    main()
