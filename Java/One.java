import java.util.*;

public class One {
    static void dfs(int[][] mat,boolean[] visited,int v){
        visited[v] = true;
        System.out.print(v+" ");
        for(int i=0;i<mat.length;i++){
            if(mat[v][i] == 1 && !visited[i]){
                dfs(mat,visited,i);
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // int n = sc.nextInt();
        int n = 8;
        int[][] mat = new int[n][n];
        mat = new int[][] {{0,1,1,1,1,0,0,0},
                        {1,0,0,0,0,1,0,0},
                        {1,0,0,0,0,1,0,0},
                        {1,0,0,0,0,0,1,0},
                        {1,0,0,0,0,0,1,0},
                        {0,1,1,0,0,0,0,1},
                        {0,0,0,1,1,0,0,1},
                        {0,0,0,0,0,1,1,0}};
        // for(int i=0;i<n;i++){
        //     for(int j=0;j<n;j++){
        //         mat[i][j] = sc.nextInt();
        //     }
        // }
        boolean[] visited = new boolean[n];
        dfs(mat,visited,2);
    };
}   
// 8
// 0 1 1 1 1 0 0 0
// 1 0 0 0 0 1 0 0
// 1 0 0 0 0 1 0 0
// 1 0 0 0 0 0 1 0
// 1 0 0 0 0 0 1 0
// 0 1 1 0 0 0 0 1
// 0 0 0 1 1 0 0 1
// 0 0 0 0 0 1 1 0
// 2