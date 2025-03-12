/*program to check whether a number is armstrong or not*/
#include<stdio.h>
void main()
{
    int a,b,c,d=0;
    printf("ENTER ANY NUMBER: ");
    scanf("%d",&a);
    b=a;
    while(a!=0)
    {
        c=a%10;           // 456
        d+=(c*c*c);
        a/=10;
    }
    if(d==b)
    {
        printf("%d IS AN AMSTRONG NUMBER",b);
    }
    else
    {
        printf("%d is not an armstrong number",b);
    }
}