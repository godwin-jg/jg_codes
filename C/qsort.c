#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<ctype.h>

int compare(const void *p1, const void *p2) {
    return strcmp(p1, p2);
}
int cmp(const void*a,const void *b){
    return (*(int*)a - *(int*)b);
}
int main() {
    char str[]="zebr\nis\nblack\nand\nwhite";
    char *p;
    p=strtok(str," ");
    while(p!=NULL){
        printf("%s",p);
        p=strtok(NULL," ");
    }
    // char str[6][25];
    // for (int i = 0; i < 5; i++) {
    //     scanf("%24s", str[i]); // Limit input to 24 characters to avoid buffer overflow
    // }

    // qsort(str, 5, sizeof(str[0]), compare);

    // for (int i = 0; i < 5; i++)
    //     printf("%s ", str[i]);
    // char str
    // scanf("%s",str);
    // char out[1000];
    // strcpy(out,strstr(str,"is"));
    // printf("%d\n",sizeof(str)/sizeof(str[0]));
    // qsort(void *base, size_t nitems, size_t size, int (*compar)(const void *, const void*))[]
    // qsort(str, sizeof(str)/sizeof(str[0]), 1, compare);
    // for(int i=0;i<sizeof(str)/sizeof(str[0]);i++){
    //     printf("%c ",toupper(str[i]));
    // }
    // printf("%s",out);

    return 0;
}