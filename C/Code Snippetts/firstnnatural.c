/*program to print the sum of first n natural numbers*/
#include<stdio.h>
void main()
{
    int n,s=0,i;
    printf("ENTER A NUMBER: ");
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
        s+=i;
    }
    printf("SUM=%d",s);
}