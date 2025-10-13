from src.tic_tac_toe.utils import ask_for_name

def main():
    print("=== Tic Tac Toe ===")

    name1 = ask_for_name("player #1")
    name2 = ask_for_name("player #2")
    print(f"Starting game for {name1} and {name2}")

if __name__ == "__main__":
    main()
