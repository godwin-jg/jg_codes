import java.util.Scanner;

public class ChessGame {
    private char[][] board;
    private String currentPlayer;

    public ChessGame() {
        initializeBoard();
        currentPlayer = "white";
    }

    private void initializeBoard() {
        board = new char[][] {
                {'r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'},
                {'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'},
                {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '},
                {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '},
                {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '},
                {' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '},
                {'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'},
                {'R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'}
        };
    }

    private void printBoard() {
        for (char[] row : board) {
            for (char square : row) {
                System.out.print(square + " ");
            }
            System.out.println();
        }
        System.out.println();
    }

    private boolean isValidMove(int startRow, int startCol, int endRow, int endCol) {
        // Implement your own logic for valid moves
        return true;
    }

    private void makeMove(int startRow, int startCol, int endRow, int endCol) {
        if (isValidMove(startRow, startCol, endRow, endCol)) {
            char piece = board[startRow][startCol];
            board[startRow][startCol] = ' ';
            board[endRow][endCol] = piece;
            switchPlayer();
        } else {
            System.out.println("Invalid move! Try again.");
        }
    }

    private void switchPlayer() {
        currentPlayer = currentPlayer.equals("white") ? "black" : "white";
    }

    public void play() {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("Current player: " + currentPlayer);
            printBoard();

            System.out.print("Enter the starting position (row col): ");
            int startRow = scanner.nextInt();
            int startCol = scanner.nextInt();

            System.out.print("Enter the ending position (row col): ");
            int endRow = scanner.nextInt();
            int endCol = scanner.nextInt();

            makeMove(startRow, startCol, endRow, endCol);
        }
    }

    public static void main(String[] args) {
        ChessGame game = new ChessGame();
        game.play();
    }
}
