#include<stdio.h>
#include<stdlib.h>

int **newMatrix(int row,int col){
    int **mat = (int**)malloc(row*sizeof(int*));
    for(int i=0;i<row;i++)
        mat[i] =(int*)malloc(col*sizeof(int*));
    return mat;
}
void getMatrix(int **mat,int r,int c){
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            scanf("%d",*(mat+i)+j);
        }
    }
}
void Print(int **mat,int r, int c){
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            printf("%d ",*(*(mat+i)+j));
        }
    }
}

// mat[i][k]*mat[k](j)
int** Multiply(int **mat1,int **mat2,int r1,int c1,int r2,int c2){
    if(c1!=r2){
        printf("Multiplication not possible");
        return 0;
    }
    int **res = newMatrix(r1,c1);
    for(int i=0;i<r1;i++){
        for(int j=0;j<c2;j++){
            *(*(res+i)+j) = 0;
            for(int k=0;k<c1;k++){
                *(*(res+i)+j) = *(*(mat1+i)+k) + *(*(mat2+k)+j);
            }
        }
    }
    return res;
}
   
int main(){
    int row = 3, col = 3;
    int **mat1 = newMatrix(row,col);
    int **mat2 = newMatrix(row,col);
    getMatrix(mat1,row,col);
    getMatrix(mat2,row,col);
    int **res = Multiply(mat1,mat2,row,col,row,col);
    Print(res,row,col);
    return 0;
}