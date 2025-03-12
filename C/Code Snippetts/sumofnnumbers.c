//program to find the sum of n numbers
#include<stdio.h>
int main(){
    int n=1,s=0,i;
    char ch='y';
    do{
        printf("ENTER NO%d: ",n);
        scanf("%d",&i);
        s+=i;
        printf("MORE TERMS?(Y/N): ");
        ch=getchar();
        n+=1;
    }while(ch=='y'||ch=='Y');
    printf("SUM OF THE GIVEN NUMBERS IS %d",s);
    return 0;
}