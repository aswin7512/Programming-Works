/*program to sort a list of numbers in ascending order*/
#include<stdio.h>
void main()
{
    int a[100],n,i,j,t;
    printf("ENTER NO. OF ELEMENTS: ");
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        printf("ENTER ELEMENT %d: ",i+1);
        scanf("%d",&a[i]);
    }
    for(i=0;i<n-1;i++)
    {
        for(j=0;j<n-1;j++)
        {
            if (a[j]>a[j+1])
            {
                t=a[j];
                a[j]=a[j+1];
                a[j+1]=t;
            }
        }
    }
    for(i=0;i<n;i++)
    {
        printf("%d ",a[i]);
    }
}