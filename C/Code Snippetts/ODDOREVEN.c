/*program to check whether a number is odd or even*/
#include<stdio.h>
void main()
{
    int a;
    printf("ENTER ANY NUMBER: ");
    scanf("%d",&a);
    if (a%2==0)
    {
        printf("%d IS AN EVEN NUMBER",a);
    }
    else
    {
        printf("%d IS AN ODD NUMBER",a);
    }
}