/*program to find the sum of 2 numbers*/
#include<stdio.h>
void main()
{
    struct sum{
        int a;
        int b;
        int t;
    }s;
    printf("ENTER 2 NUMBERS: ");
    scanf("%d %d",&s.a,&s.b);
    s.t=s.a+s.b;
    printf("SUM OF %d & %d=%d",s.a,s.b,s.t);
}