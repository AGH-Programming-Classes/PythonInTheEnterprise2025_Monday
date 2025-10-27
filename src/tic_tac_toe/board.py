class Board:
    def __init__(self, size = 3):
        self.size = size
        self.board_state = [[' '] * size for _ in range(size)]

    # board_state: char[3][3]
    def draw(self):
        spacer_size = 4 * self.size + 1
        print("-" * spacer_size)
        for i in range(self.size):
            print("|", end="")
            for j in range(self.size):
                to_print = self.board_state[i][j] if self.board_state[i][j] != ' ' else (self.size * i + j + 1)
                print(f" {to_print} |", end="")
            print()
            print("-" * spacer_size)
    
    def setCell(self, idx, value):
        i = (idx - 1) // self.size
        j = (idx - 1) % self.size
        self.board_state[i][j] = value

    def getBoardState(self):
        return self.board_state

    