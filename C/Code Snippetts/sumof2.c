/*program to find the sum of 2 numbers using pointer and structure*/
#include<stdio.h>
void main()
{
    struct sum{
        int a;
        int b;
        int s;
    }*pi;
    printf("ENTER 2 NUMBERS: ");
    scanf("%d %d",&pi->a,&pi->b);
    pi->s=pi->a+pi->b;
    printf("SUM=%d",pi->s);
}