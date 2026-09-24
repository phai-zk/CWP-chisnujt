ROOK_MOVE = [(1, 0), (-1, 0), (0, 1), (0, -1)]
BISHOP_MOVE = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
PAWN_MOVE = [(-1, -1), (-1, 1)]
QUEEN_MOVE = ROOK_MOVE + BISHOP_MOVE
PIECE_SET = ["K", "Q", "R", "B", "P"]

def handle_boundary(i: int, j: int, size) -> bool:
    return i < 0 or i >= size or j < 0 or j >= size

def get_move_set(piece: str):
    return PAWN_MOVE if piece == "P" \
        else BISHOP_MOVE if piece == "B" \
        else ROOK_MOVE if piece == "R" \
        else QUEEN_MOVE if piece == "Q" else None

def move(i: int, j: int, board: list, size:int) -> bool:
    move_set = get_move_set(board[i][j])
    if move_set is None: 
        return False
    if board[i][j] == "P":
        for dx, dy in move_set:
            x = i + dx
            y = j + dy
            if not handle_boundary(x, y, size) and board[x][y] == "K":
                return True
        return False

    for dx, dy in move_set:
        x = i + dx
        y = j + dy
        while not handle_boundary(x, y, size):
            if board[x][y] == "K":
                return True
            if board[x][y] in PIECE_SET:
                break
            x += dx
            y += dy
    return False

def create_board(board: str) -> list:
    if board is None or str(board).strip() == "":
        print("Error: A board is empty!")
        return

    king_count = board.count("K")
    if king_count == 0:
        print("Error: Have no one King on the board!")
        return
    if king_count > 1:
        print("Error: Have more than one King!")
        return

    board = [list(line) for line in board.strip().splitlines()]
    max_row = len(board)
    max_col = len(board[0])

    if max_row != max_col or any(len(row) != max_col for row in board):
        print(f"Error: A board {max_row} x {max_col} is not a square!")
        return
    return board

def checkmate(board: str):
    board = create_board(board)
    if board is None:
        return
    size = len(board)
    for i in range(size):
        for j in range(size):
            if move(i, j, board, size):
                print("Success")
                return
    print("Fail")

if __name__ == "__main__":
    checkmate()