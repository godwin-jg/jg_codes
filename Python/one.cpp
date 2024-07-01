// C++ code to implement the approach
#include <bits/stdc++.h>
using namespace std;

// DP table initialized with -1
int dp[11][2][(1LL << 10) - 1][2];

int recur(int i, int j, int k, int l, string a) {
  // Base case
  if (i == a.size()) {
    return 1;
  }

  // If answer for current state is already
  // calculated then just return dp[i][j][k]
  if (dp[i][j][k][l] != -1)
    return dp[i][j][k][l];

  // Answer initialized with zero
  int ans = 0;

  // Tight condition true
  if (j == 1) {

    // Iterating from 0 to max value of
    // tight condition
    for (int digit = 0; digit <= 9; digit++) {

      // mask for digit
      int mask = (1 << digit);

      // if that digit is available to use
      if (mask & k) {

        // calling recursive function for max digit
        // taken and retaining tight condition
        if (digit == ((int)a[i] - 48)) {
          ans += recur(i + 1, 1, k - (1 << digit), 1, a);
        }

        // calling recursive function for zero
        // and dropping tight condition
        else if (digit == 0) {
          ans += recur(i + 1, 0, k, 0, a);
        }

        // calling recursive function for number
        // less than max and dropping condition
        else if (digit < ((int)a[i] - 48)) {
          ans += recur(i + 1, 0, k - (1 << digit), 1, a);
        }
      }
    }
  }

  // Tight condition false
  else {

    // Iterating for all digits
    for (int digit = 0; digit <= 9; digit++) {
      int mask = (1 << digit);

      if (mask & k) {
        // calling recursive function for
        // not taking anything
        if (digit == 0 and l == 0)
          ans += recur(i + 1, 0, k, 0, a);

        // calling recursive function for
        // taking zero
        else if (digit == 0 and l == 1)
          ans += recur(i + 1, 0, k - (1 << digit), 1, a);

        // calling recursive function for taking
        // digits from 1 to 9
        else
          ans += recur(i + 1, 0, k - (1 << digit), 1, a);
      }
    }
  }

  // Save and return dp value
  return dp[i][j][k][l] = ans;
}

// Function to find numbers
// in the range L to R such that its
// digits are distinct
int countInRange(int A, int B) {

  // Initializing dp array with - 1
  memset(dp, -1, sizeof(dp));

  A--;
  string L = to_string(A), R = to_string(B);

  // Numbers with distinct digits in range 0 to L
  int ans1 = recur(0, 1, (1 << 10) - 1, 0, L);

  // Initializing dp array with - 1
  memset(dp, -1, sizeof(dp));

  // Numbers with distinct digits in range 0 to R
  int ans2 = recur(0, 1, (1 << 10) - 1, 0, R);

  // Difference of ans2 and ans1
  // will generate answer for required range
  return ans2 - ans1;
}

// Driver Code
int main() {
  // Input 1
  int L = 9, R = 19;

  // Function Call
  cout << countInRange(L, R) << endl;
  return 0;
}
