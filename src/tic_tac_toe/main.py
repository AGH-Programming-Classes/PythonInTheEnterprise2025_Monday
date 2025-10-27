from tic_tac_toe.game import Gameplay
from tic_tac_toe.player import *

def main():
    g = Gameplay(Player('X', Manual()), Player('O', Random()))
    g.start()

if __name__ == "__main__":
    main()