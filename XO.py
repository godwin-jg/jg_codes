class Grid:
    def __init__(self, size):
        self.size = size
        self.grid = [[' ' for i in range(size)] for j in range(size)]
        
    def print_grid(self):
        for i in range(self.size):
            print('|'.join(self.grid[i]))
            if i < self.size - 1:
                print('-' * (self.size * 2 - 1))
                
    def update_grid(self, x, y, player):
        if self.grid[x][y] == ' ':
            self.grid[x][y] = player
            return True
        return False
    
    def check_win(self, connectN, player):
        # check rows
        for i in range(self.size):
            count = 0
            for j in range(self.size):
                if self.grid[i][j] == player:
                    count += 1
                else:
                    count = 0
                if count == connectN:
                    return True
        # check columns
        for i in range(self.size):
            count = 0
            for j in range(self.size):
                if self.grid[j][i] == player:
                    count += 1
                else:
                    count = 0
                if count == connectN:
                    return True
        # check diagonals
        for i in range(self.size):
            count = 0
            for j in range(self.size):
                if i + j < self.size:
                    if self.grid[i + j][j] == player:
                        count += 1
                    else:
                        count = 0
                    if count == connectN:
                        return True
                if i + j < self.size:
                    if self.grid[j][i + j] == player:
                        count += 1
                    else:
                        count = 0
                    if count == connectN:
                        return True
        return False
    
    def check_draw(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] == ' ':
                    return False
        return True
    
    def reset_grid(self):
        self.grid = [[' ' for i in range(self.size)] for j in range(self.size)]
        
        
class Game:
    def __init__(self, size, connectN):
        self.size = size
        self.connectN = connectN
        self.grid = Grid(size)
        self.player1 = 'X'
        self.player2 = 'O'
        self.current_player = self.player1
        
    def play(self):
        self.grid.print_grid()
        while True:
            print("Player {}'s turn".format(self.current_player))
            x = int(input("Enter x: "))
            y = int(input("Enter y: "))
            if self.grid.update_grid(x, y, self.current_player):
                self.grid.print_grid()
                if self.grid.check_win(self.connectN, self.current_player):
                    print("Player {} wins".format(self.current_player))
                    break
                if self.grid.check_draw():
                    print("Draw")
                    break
                if self.current_player == self.player1:
                    self.current_player = self.player2
                else:
                    self.current_player = self.player1
        self.grid.reset_grid()
        
game = Game(6,3)
game.play()