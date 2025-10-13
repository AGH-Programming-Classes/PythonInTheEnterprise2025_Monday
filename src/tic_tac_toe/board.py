class Board:
    def __init__(self):
        yield

    # board_state: char[3][3]
    def draw(self, board_state):
        print("-" * 7)
        for i in range(3):
            print("|", end="")
            for j in range(3):
                print(f"{board_state[i][j]}|", end="")
            print("\n-" * 7)

    