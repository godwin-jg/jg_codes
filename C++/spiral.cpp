#include <bits/stdc++.h>
using namespace std;

int main() {
  int mat[4][4] = {
      {1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 16}};
  int rowstart = 0, colstart = 0;
  int rowend = sizeof(mat) / sizeof(mat[0]) - 1,
      colend = sizeof(mat[0]) / sizeof(mat[0][0]) - 1;

  while (rowstart <= rowend && colstart <= colend) {
    for (int i = colstart; i <= colend; i++) {
      cout << mat[rowstart][i] << " ";
    }
    rowstart++;
    for (int i = rowstart; i <= rowend; i++) {
      cout << mat[i][colend] << " ";
    }
    colend--;
    for (int i = colend; i >= colstart; i--) {
      if (rowstart > rowend)
        break;
      cout << mat[rowend][i] << " ";
    }
    rowend--;
    for (int i = rowend; i >= rowstart; i--) {
      if (colstart > colend)
        break;
      cout << mat[i][colstart] << " ";
    }
    colstart++;
  }
}