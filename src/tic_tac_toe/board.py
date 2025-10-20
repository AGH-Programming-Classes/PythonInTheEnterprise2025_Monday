class Board:
    def __init__(self, size: int):
        self.size = size
        self.board_state = [[' '] * size for _ in range(size)]

    # board_state: char[3][3]
    def draw(self):
        self._draw(self.board_state)
        
    def draw_board_idx(self):
        self._draw([[f'{i * self.size + j + 1}' for j in range(self.size)] for i in range(self.size)])
    
    def setCell(self, idx, value):
        i = (idx - 1) // self.size
        j = (idx - 1) % self.size
        print(i, j)
        self.board_state[i][j] = value

    def getBoardState(self):
        return self.board_state

    def _draw(self, data):
        spacer_size = 4 * self.size + 1
        print("-" * spacer_size)
        for i in range(self.size):
            print("|", end="")
            for j in range(self.size):
                print(f" {data[i][j]} |", end="")
            print()
            print("-" * spacer_size)
    