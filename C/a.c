
#include <stdio.h>
#include <string.h>


// int main(){
//     union abc
//     {
//         int a;
//         int b;
//         struct c{
//             char d;
//             int y;/* data */
//         };
//         struct d{
//             char ad;
//             char ab;
//         };
   
//     };
//     printf("%d",sizeof(abc));
// }
#include <stdio.h>
#include <string.h>
#include <stdlib.h>


// void funct(char*p){
//     p = (char*)malloc(10);
//     strcpy(p,"hello");
//     return;
// }
#define CUBE(x)(x*x*x)



int main() {
    int a= 3;
    int b;
    b = CUBE(a++);
    printf("%dn",b);
}
