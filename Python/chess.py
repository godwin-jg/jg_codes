import chess.Board
# import chess.svg
from IPython.display import display, HTML, SVG

def display_board(board):
    display(SVG(chess.svg.board(board=board)))

def play_chess():
    board = chess.Board()

    while not board.is_game_over():
        display_board(board)
        legal_moves = [str(move) for move in board.legal_moves]
        print("Legal moves:", legal_moves)

        move_uci = input("Enter your move in UCI format (e.g., e2e4): ")
        if move_uci not in legal_moves:
            print("Invalid move! Try again.")
            continue

        move = chess.Move.from_uci(move_uci)
        board.push(move)

    display_board(board)
    result = board.result()
    print("Game Over. Result: " + result)

if __name__ == "__main__":
    play_chess()
