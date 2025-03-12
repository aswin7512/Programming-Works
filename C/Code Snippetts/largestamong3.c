/*program to find the largest among 3 numbers*/
#include<stdio.h>
void main()
{
    int a,b,c,d;
    printf("ENTER 3 NUMBER:");
    scanf("%d %d %d",&a,&b,&c);
    d=a>b?a:b;
    d=d>c?d:c;
    printf("Largest number=%d",d);
}