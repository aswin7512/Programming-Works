/*program to print the fibonacci series*/
#include<stdio.h>
void main()
{
    int fib(int);
    int a,i;
    printf("ENTER ANY NUMBER: ");
    scanf("%d",&a);
    for(i=1;i<a+1;i++)
    {
        printf("%d ",fib(i));
    }
}
int fib(int n)
{
    if(n==1 || n==2)
    {
        return 1;
    }
    else
    {
        return fib(n-1)+fib(n-2);
    }
}