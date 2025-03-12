/*program to find the sum of two numbers using function*/
#include<stdio.h>
void main()
{
    int sum(int,int);
    int a,b,s;
    printf("ENTER 2 NUMBERS: ");
    scanf("%d %d",&a,&b);
    s=sum(a,b);
    printf("SUM=%d",s);
}
int sum(int x,int y)
{
    int s1;
    s1=x+y;
    return s1;
}