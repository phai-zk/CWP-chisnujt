import sys
from pathlib import Path
from checkmate import checkmate

def main():
    files = sys.argv[1:]
    for file in files:
        try:
            board = Path(file).read_text(encoding="utf-8")
            checkmate(board)
        except FileNotFoundError:
            print(f"Error: Not found {file}")

if __name__ == "__main__":
    main()