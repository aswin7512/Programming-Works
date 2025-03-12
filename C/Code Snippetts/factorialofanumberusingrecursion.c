/*program to find the factorial of a number using recursion*/
#include<stdio.h>
void main()
{
    int fact(int);
    int a,f;
    printf("ENTER ANY NUMBER: ");
    scanf("%d",&a);
    f=fact(a);
    printf("FACTORIAL OF %d=%d",a,f);
}
int fact(int a)
{
    if (a==0 || a==1)
    {
        return 1;
    }
    else
    {
        return a*fact(a-1);
    }
}