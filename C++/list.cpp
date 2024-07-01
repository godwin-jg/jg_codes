#include <iostream>
using namespace std;

class Node {
public:
  int data;
  Node *next;

  Node(int x) {
    data = x;
    next = NULL;
  }
};

class LinkedList {
public:
  Node *head;

  LinkedList() { head = NULL; }

  void insert(int x) {
    if (head == NULL) {
      head = new Node(x);
      return;
    }
    Node *temp = head;
    Node *newNode = new Node(x);
    while (temp->next != NULL) {
      temp = temp->next;
    }
    temp->next = newNode;
  }

  void insertInOrder(int x) {
    if (head == NULL || x < head->data) {
      Node *newNode = new Node(x);
      newNode->next = head;
      head = newNode;
      return;
    }
    Node *temp = head;
    while (temp->next != NULL && x > temp->next->data) {
      temp = temp->next;
    }
    Node *newNode = new Node(x);
    newNode->next = temp->next;
    temp->next = newNode;
  }

  void Print() {
    Node *temp = head;
    while (temp != NULL) {
      cout << temp->data << " ";
      temp = temp->next;
    }
    cout << endl;
  }
};

int main() {
  int arr[] = {1, 3, 4, 5, -2, -1};
  LinkedList list;
  for (int i = 0; arr[i] != -1; i++) {
    list.insertInOrder(arr[i]);
  }
  list.Print();
}