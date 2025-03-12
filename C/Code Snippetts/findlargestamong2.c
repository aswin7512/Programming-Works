/*program to find the largest among 2 numbers*/
#include<stdio.h>
void main()
{
    int a,b,c;
    printf("ENTER 2 NUMBER: ");
    scanf("%d %d",&a,&b);
    c=a>b?a:b;
    printf("Largest number=%d",c);
}