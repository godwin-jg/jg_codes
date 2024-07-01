#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int max(int a,int b){
    return a > b ? a : b;
}
int main(){
    int n = 5;
    int rows = n; // 4
    int cols = -n; // -4

    for(int i=rows;i>=-n;i--){
        for(int j=cols;j<=n;j++){
            int d = max(abs(i),abs(j))+1;
            printf("%d ",d);
        }
        puts("");
    }  
}