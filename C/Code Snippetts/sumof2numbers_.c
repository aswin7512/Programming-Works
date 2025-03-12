/*program to find the sum of 2 numbers using pointers*/
#include<stdio.h>
void main()
{
    int *pi,*pj,s,a,b;
    printf("ENTER TWO NUMBERS: ");
    scanf("%d %d",&a,&b);
    pi=&a;
    pj=&b;
    s=*pi+ *pj;
    printf("SUM=%d",s);
}