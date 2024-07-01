#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

// #include <bits/stdc++.h>
using namespace std;

int main() {
  vector<int> arr = {-11, 5, 2, 3, 3, 5};
  vector<int> vec2(5, 0);
  fill(vec2.begin(), vec2.end(), 1);
  // ranges::sort(arr);
  vector<int> vec3(5, 0);
  int x = count(arr.begin(), arr.end(), 3);
  //   cout << x << endl;
  arr.insert(arr.begin() + 2, 4);
  for (int i = 0; i < arr.size(); i++) {
    cout << arr[i] << " ";
  }

  // Create a map with string keys and int values
  map<string, int> myMap;

  // Insert key-value pairs into the map
  myMap["apple"] = 5;
  myMap["banana"] = 3;
  myMap["orange"] = 7;

  // Access and modify values in the map
  myMap["apple"] += 2;

  // Iterate over the map and print key-value pairs
  for (const auto &[key, value] : myMap) {
    cout << key << " => " << value << '\n';
  }

  for (const auto &pair : myMap) {
    cout << pair.first << ": " << pair.second << endl;
  }
  for (auto it = myMap.begin(); it != myMap.end(); ++it) {
    std::cout << it->first << " => " << it->second << '\n';
  }
  if (myMap.find("banan=a") != myMap.end()) {
    cout << "Found banana" << endl;
    myMap["banana"] = 10;
  }

  return 0;
}
