from gamefunctions import *
import os

## version with class

class Game(Subject):
    def __init__(self):
        super().__init__()
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.observers = []
        # default players; will be set at start of play
        self.playerO = Player('O', HumanMoveStrategy())
        self.playerX = Player('X', HumanMoveStrategy())
        #self.playerO = Player('O', self)
        #self.playerX = Player('X', self)

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)
    def reset_board(self):
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]


    def play(self):
        try:
            mode = input("Would you like to play against another person(1) or are you playing alone(2)? ").strip()
            if mode == '1':
                self.playerO = Player('O', HumanMoveStrategy())
                self.playerX = Player('X', HumanMoveStrategy())
            else:
                self.playerO = Player('O', HumanMoveStrategy())
                self.playerX = Player('X', ComputerMoveStrategy())
        except ValueError:
            print("Invalid input! Please enter correct number.")
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print_board(self.board)
        self.notify("New game started")

        while True:
            print("O's turn, make a move:")
            self.playerO.play(self)
            os.system('cls' if os.name == 'nt' else 'clear')
            print_board(self.board)
            if winning_move(self.board, 'O'):
                self.notify("O has won the game!")
                break
            
            ## Check for draw (no more empty cells)
            if not any(' ' in row for row in self.board):
                self.notify("The game ended in a draw.")
                break

            ## Player X's turn
            print("X's turn, make a move:")
            self.playerX.play(self)
            os.system('cls' if os.name == 'nt' else 'clear')
            print_board(self.board)
            if winning_move(self.board, 'X'):
                self.notify("X has won the game!")
                break

            ## Check for draw (no more empty cells)
            if not any(' ' in row for row in self.board):
                self.notify("The game ended in a draw.")
                break

        self.notify("Game over.")
        print("Thanks for playing!")
        

    def make_move(self, mark):
        move_done = False
        has_row = False
        has_col = False
        while (move_done == False):
            while (has_row == False):
                try:
                    # checking if user wants to exit
                    row_input = input("Enter row (1-3) or press q to exit: ").strip()
                    if row_input .lower()== 'q':
                        self.notify("The game was stopped by the user.")
                        print("Thanks for playing!")
                        exit()
                    row = int(row_input) - 1
                    if row not in range(3):
                        print("Invalid row number! Please enter a number between 1 and 3.")
                        continue
                    else:
                        has_row = True
                #error if NaN
                except ValueError: 
                    print("Invalid input! Please enter numbers only.")
                    continue
            while (has_col == False):
                try:              
                    col_input = input("Enter column (1-3) or press q to exit: ").strip()
                    if col_input.lower() == 'q':
                        self.notify("The game was stopped by the user.")
                        print("Thanks for playing!")
                        exit()
                    col = int(col_input) - 1
                    if col not in range(3):
                        print("Invalid col number! Please enter a number between 1 and 3.")
                        continue
                    else:
                        has_col = True
                #error if NaN
                except ValueError: 
                    print("Invalid input! Please enter numbers only.")
                    continue

            #checking if empty
            if self.board[row][col] == ' ':
                self.board[row][col] = mark
                move_done = True
                self.notify(f"Player {mark} placed his mark on row {row + 1}, column {col + 1}")
            else:
                has_col = False
                has_row = False
                print("Invalid move! There's already a mark in the specified position!")
                continue


if __name__ == "__main__":


    game = Game()
    game_logger = Logger()
    game_console = Console()
    game.add_observer(game_logger) 
    game.add_observer(game_console)
    
    while True:
        game.reset_board()
        game.play()
        cont = input(("Do you want to play a new game? Press y for yes or n for no.").strip())
        while (cont != 'n' and cont != 'y'):
            print("Wrong character! Entry only n or y!")
            print()
            cont = input(("Press y for yes or n for no. ").strip())
        if(cont == 'n'):
            break
        else:
            continue
        
