class ChessGame:
    def __init__(self):
        self.board = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
                      ['p'] * 8,
                      [' '] * 8,
                      [' '] * 8,
                      [' '] * 8,
                      [' '] * 8,
                      ['P'] * 8,
                      ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]
        self.current_player = 'white'

    def print_board(self):
        for row in self.board:
            print("|".join(row),end="__")
        print()

    def is_valid_move(self, start, end):
        # Implement your own logic for valid moves
        return True

    def make_move(self, start, end):
        if self.is_valid_move(start, end):
            piece = self.board[start[0]][start[1]]
            self.board[start[0]][start[1]] = ' '
            self.board[end[0]][end[1]] = piece
            self.switch_player()
        else:
            print("Invalid move! Try again.")

    def switch_player(self):
        self.current_player = 'black' if self.current_player == 'white' else 'white'

    def play(self):
        while True:
            print(f"Current player: {self.current_player.capitalize()}")
            self.print_board()
            start = tuple(map(int, input("Enter the starting position (row col): ").split()))
            end = tuple(map(int, input("Enter the ending position (row col): ").split()))

            self.make_move(start, end)


if __name__ == "__main__":
    game = ChessGame()
    game.play()
