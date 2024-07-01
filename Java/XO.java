import java.util.Scanner;

public class XO {
    private char[][] board;
    private char currentPlayer;
    public XO() {
        initializeBoard();
        currentPlayer = 'X';
    } 
    
    private void initializeBoard(){
        board = new char[3][3];
        for(int i=0;i<3;i++){
            for(int j=0;j<3;j++){
                board[i][j] = '_';
            }
        }

    }
    private void printBoard(){
        for(char[] row: board){
            for(char c: row){
                System.out.print(c+" ");
            }
            System.out.println();
        }
        System.out.println();
    }

    private boolean isValidMove(int row,int col){
        if (row<0 || col<0 || row>2 || col>2) 
            return false;
        if (board[row][col] != '_')
            return false;
        return true;
    }
    
    private void switchPlayer(){
        currentPlayer = currentPlayer == 'X' ? '0' : 'X';
    }
    
    private void makeMove(int row,int col){
        if(isValidMove(row, col)){
            board[row][col] = currentPlayer;
            if (checkwin()) {
                System.out.println(currentPlayer + "WON"); printBoard();
                System.exit(0);
            }
            switchPlayer();
        }else{
            System.out.println("Invalid Move.Try Again");
        }

    }
    private boolean checkwin(){
        //checkcols
        for(int i=0;i<3;i++){
            if(board[0][i] == board[1][i] && board[1][i] == board[2][i] && board[0][i] == currentPlayer)
            return true;
        }
        //checkrows
        for(int i=0;i<3;i++){
            if(board[i][0] == board[i][1] && board[i][1] == board[i][1] && board[i][0] == currentPlayer)
            return true;
        }
        //checkposdiag
        if(board[0][0] == board[1][1] && board[1][1] == board[2][2] && board[1][1] == currentPlayer) return true;
        //checknegdiag
        if(board[0][2] == board[1][1] && board[1][1] == board[2][0] && board[1][1] == currentPlayer) return true;

        return false;
    }
   
    public void play(){
        Scanner scanner = new Scanner(System.in);
        while(true){
            System.out.println("Current player: " + currentPlayer);
            printBoard();
            int col = 0,row = 0;
            System.out.println("Enter row: ");
            row = scanner.nextInt();
            System.out.println("Enter column: ");
            col = scanner.nextInt();
            makeMove(row,col);
           
        }
    }

    public static void main(String[] args) {
        XO xo = new XO();
        xo.play();
    }

}
