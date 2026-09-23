ROOK_MOVE = [(1, 0), (-1, 0), (0, 1), (0, -1)]
BISHOP_MOVE = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
PAWN_MOVE = [(-1, -1), (-1, 1)]
QUEEN_MOVE = ROOK_MOVE + BISHOP_MOVE
PIECE_SET = ["K", "Q", "R", "B", "P"]
max_row = 8
max_col = 8

def handle_boundary(i: int, j: int) -> bool:
    return i < 0 or i >= max_row or j < 0 or j >= max_col

def move(i: int, j: int, board: list, move_set: list) -> bool:
    if board[i][j] == "P":
        for dx, dy in move_set:
            x = i + dx
            y = j + dy
            if not handle_boundary(x, y) and board[x][y] == "K":
                return True
        return False

    for dx, dy in move_set:
        x = i + dx
        y = j + dy
        while not handle_boundary(x, y):
            if board[x][y] == "K":
                return True
            if board[x][y] in PIECE_SET:
                break
            x += dx
            y += dy

    return False

def piece_check(i: int, j: int, board: list) -> bool:
    if board[i][j] == "P":
        return move(i, j, board, PAWN_MOVE)
    elif board[i][j] == "R":
        return move(i, j, board, ROOK_MOVE)
    elif board[i][j] == "B":
        return move(i, j, board, BISHOP_MOVE)
    elif board[i][j] == "Q":
        return move(i, j, board, QUEEN_MOVE)
    return False

def create_board(board: list) -> None:
    global max_row, max_col
    king_count = board.count("K")

    if board is None or str(board).strip() == "":
        print("Error: A board is empty!")
        return

    if king_count == 0:
        print("Error: Have no one King on the board!")
        return

    if king_count > 1:
        print("Error: Have more than one King!")
        return
    
    board = [list(line) for line in board.strip().splitlines()]
    max_row = len(board)
    max_col = len(board[0])
    col_set = set([len(x) for x in board])

    # print(board)
    # print(f"{max_row} {max_col} {len(col_set)}")

    if (max_row != max_col) or (len(col_set) > 1) :
        print(f"Error: A board {max_row} x {max_col} is not a square!")
        return

    if max_row > 8 or max_col > 8:
        print(f"Error: The board is too big!")
        return

    return board

def checkmate(board: str):
    board = create_board(board)

    if board is not None:
        for i in range(max_row):
            for j in range(max_col):
                if piece_check(i, j, board):
                    print("Success")
                    return
        print("Fail")
        