/*program to find the largest number in an array*/
#include<stdio.h>
void main()
{
    int a[100],n,i,l;
    printf("ENTER THE NO. OF NUMBERS: ");
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        printf("ENTER ELEMENT %d",i+1);
        scanf("%d",&a[i]);
    }
    l=a[0];
    for(i=1;i<n;i++)
    {
        if (l<a[i])
        {
            l=a[i];
        }
    }
    printf("LARGEST NUMBER IS: %d",l);
}