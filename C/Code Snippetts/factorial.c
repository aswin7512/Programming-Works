/*program to print the factorial of a number*/
#include<stdio.h>
void main()
{
    int a,i,f=1;
    printf("ENTER A NUMBER: ");
    scanf("%d",&a);
    for(i=1;i<=a;i++)
    {
        f*=i;
    }
    printf("FACTORIAL=%d",f);
}