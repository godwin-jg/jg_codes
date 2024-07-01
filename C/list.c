#include<stdio.h>
#include<stdlib.h>
struct Node
{
    int data;
    struct Node *next;
}*head=NULL;

struct Node* getNode(int x){
    struct Node* node = (struct Node*)malloc(sizeof(struct Node));
    node->data = x;
    node->next = NULL;
    return node;
} 
void insert(int x){
    if(head==NULL){
        head = getNode(x);
        return;
    }
    struct Node* temp = head;
    struct Node* Node = getNode(x);
    while(temp->next!=NULL){
        temp = temp->next;
    }
    temp->next = Node;
}
void insertInOrder(int x){
    if (head==NULL){
        head = getNode(x);
        return;
    }
    if (x<head->data){
        struct Node* node = getNode(x);
        node->next = head;
        head = node;
        return;
    }
    struct Node* temp = head;
    while(temp->next!=NULL && x>temp->next->data)
        temp = temp->next;
    struct Node* node = getNode(x);
    node->next = temp->next;
    temp->next = node;
}
// void delete(int x){
//     if ()
// }
void Print(){
    struct Node* temp = head;
    while(temp!=NULL){
        printf("%d ",temp->data);
        temp = temp->next;
    }
    printf("\n");
}
int main(){
    int arr[] = {1,3,4,5,-1};
    struct Node* head = NULL;
    for(int i=0;arr[i];i++){
       insertInOrder(arr[i]);
    }
    Print();
}