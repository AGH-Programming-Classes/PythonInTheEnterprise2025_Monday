from gamefunctions import *
import os


# board = [
#     [' ', ' ', ' '],
#     [' ', ' ', ' '],
#     [' ', ' ', ' ']
# ]

# logger("New turn started")
# print_board(board)
# while True:
    
#     ## Player O's turn
#     print("O's turn, make a move:")
#     make_move(board, 'O')
#     os.system('cls' if os.name == 'nt' else 'clear')
#     print_board(board)
#     if winning_move(board, 'O'):
#         print("O wins!")
#         logger("O has won the game")
#         break
#     ## Player X's turn
#     if not any(' ' in row for row in board):
#         print("It's a draw!")
#         logger("The game ended in a draw")
#         break
#     print("X's turn, make a move:")
#     make_move(board, 'X')
#     os.system('cls' if os.name == 'nt' else 'clear')
#     print_board(board)
#     if winning_move(board, 'X'):
#         print("X wins!")
#         logger("X has won the game")
#         break
#     ## Check for draw (no more empty cells)


# print("Thanks for playing!")

## version with class

class Game(Subject):
    def __init__(self):
        super().__init__()
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        try:
            mode = input("Would you like to play against another person(1) or are you playing alone(2)?").strip()
            if mode == '1':
                self.playerO = Player('O', HumanMoveStrategy())
                self.playerX = Player('X', HumanMoveStrategy())
            else:
                self.playerO = Player('O', HumanMoveStrategy())
                self.playerX = Player('X', ComputerMoveStrategy())
        except ValueError:
            print("Invalid input! Please enter correct number.")
            
    def play(self):
        print_board(self.board)
        self.notify("start", {"message": "New game started"})

        while True:
            print("O's turn: ")
            self.playerO.play(self.board)
            os.system('cls' if os.name == 'nt' else 'clear')
            print_board(self.board)
            if winning_move(self.board, 'O'):
                print("O wins!")
                logger("O has won the game")
                break

            if not any(' ' in row for row in self.board):
                print("It's a draw")
                logger("The game ended in a draw")
                break

            print("X's turn: ")
            self.playerX.play(self.board)
            os.system('cls' if os.name == 'nt' else 'clear')
            print_board(self.board)
            if winning_move(self.board, 'X'):
                print("X wins!")
                logger("X has won the game")
                break


if __name__ == "__main__":
    game = Game()
    game.play()
        

