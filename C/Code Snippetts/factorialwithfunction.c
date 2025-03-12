/*program to find the factorial of a number using functions*/
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
    int i,f=1;
    for(i=1;i<a+1;i++)
    {
        f*=i;
    }
    return f;
}