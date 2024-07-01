#include <iostream>
#include <set>
#include <string>
#include <unordered_map>

using namespace std;

unordered_map<string, int> memo[11];

int dfs(string &num1, string &num2, int i, bool bounded_lower,
        bool bounded_upper, set<int> &digits, int current_number) {
  if (i == num1.size()) {
    return 1;
  }

  string key(digits.begin(), digits.end());
  if (memo[i].count(key)) {
    return memo[i][key];
  }

  int lower = bounded_lower ? (num1[i] - '0') : 0;
  int upper = bounded_upper ? (num2[i] - '0') : 9;

  int count = 0;
  for (int digit = lower; digit <= upper; ++digit) {
    if (digits.count(digit)) {
      continue;
    }

    int next_number = current_number * 10 + digit;
    if (next_number != 0) {
      digits.insert(digit);
    }
    count += dfs(num1, num2, i + 1, bounded_lower && digit == lower,
                 bounded_upper && digit == upper, digits, next_number);
    digits.erase(digit);
  }

  memo[i][key] = count;

  return count;
}

int uniqueDigits(int L, int R) {
  string num1 = to_string(L);
  string num2 = to_string(R);
  size_t n = num1.size();
  size_t m = num2.size();
  num1 = string(m - n, '0') + num1;
  set<int> digits;
  return dfs(num1, num2, 0, true, true, digits, 0);
}

int main() {
  int L = 9;
  int R = 19;
  cout << uniqueDigits(L, R) << endl;
  return 0;
}
